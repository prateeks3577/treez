# this is server file
# 1. runs a flask wsgi app
# 2. manages transaction to DB
# 3. other operations
# API list:
# POST
# init - flush existing DB, create tables with schema, create default reserve account
# transfer - transfers money
# GET
# statement - responds with money in account and all transactions
# sanity - runs through all account balance, should not be more than reserve

# create a flask app

from flask import Flask, abort, jsonify 
from waitress import serve
import logging
import sqlite3
from flask import g
import sqlite3
import random
from datetime import datetime

logging.basicConfig(format='%(asctime)s:%(threadName)s:%(message)s',filename='debug.log', encoding='utf-8', level=logging.DEBUG)

app = Flask(__name__)





##############################################################################################
####TODO: seperate file#############   DB UTILS        #######################################
##############################################################################################

DATABASE = 'database.db'

# just get the db connection on every request
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE, timeout=10)
    return db

# initialize the database, done just once
def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

# execute a query to fetch
def query_db(step,query, args=(), one=False):
    conn = get_db()
    try:
        with conn:  # manages transactino or all rollbacks!
            cursor = conn.execute(query, args)
            rv = cursor.fetchall()
            return (rv[0] if rv else None) if one else rv
    except sqlite3.OperationalError as err:
        abort(400, step+":"+str(err))
    except sqlite3.IntegrityError as err:
        abort(400, step+":"+str(err))

def executestatements(sqls):
    conn = get_db()
    with conn:
        cursor = conn.cursor()
        for sql in sqls:
            cursor.execute(sql)

# executes many
def executemanydata(step,stmt,values):
    conn = get_db()
    try:
        with conn:
            cursor = conn.cursor()
            cursor.executemany(stmt, values)
    except sqlite3.OperationalError as err:
        abort(400, step+":"+str(err))
    except sqlite3.IntegrityError as err:
        abort(400, step+":"+str(err))

# for error handling
class ValidationException(Exception):
    pass

# executes just one
def executemanydefault(step,stmt,values):
    conn = get_db()
    try:
        cursor = conn.cursor()
        cursor.execute(stmt, values[0])
        rv = cursor.lastrowid
        return rv
    except sqlite3.OperationalError as err:
        abort(400, step+":"+str(err))
    except sqlite3.IntegrityError as err:
        abort(400, step+":"+str(err))

# transfer
def TRANSFER(fromacc , toacc, amt):
    conn = get_db()

    logging.debug("%s: checking TRANSFER",__name__)
    
    try:
        with conn:  # manages transactino or all rollbacks!
            # fetch the current balance for from account            
            to_rec = query_db("Fetching accounts","SELECT * FROM ACCOUNTS WHERE ACCOUNTID = "+str(toacc))
            logging.debug('%s: validating if both account is valid',__name__)
            if len(to_rec) == 0:
                raise ValidationException("Invalid to account!")

            res = query_db("Fetching accounts","SELECT * FROM ACCOUNTS WHERE ACCOUNTID = "+str(fromacc))
            logging.debug('%s: validating if both account is valid',__name__)
            if len(res) == 0:
                raise ValidationException("Invalid from account!")

            from_acc_bal = res[0][2] - amt
            to_acc_bal = to_rec[0][2] + amt

            logging.debug('%s: validating if amount is positive %d',__name__,from_acc_bal)
            if int(from_acc_bal) < 0:                
                raise ValidationException("Insufficient Balance!")

            #logging.debug('%s: validating if last transaction was not the same and within 1 minute lastid %d',__name__,str(res[0][3]))
            currtime = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
            prevledger = query_db("Fetching ledger","SELECT * FROM LEDGER WHERE UNIQUEID = "+str(res[0][3]))
            if len(prevledger) > 0:
                #check if similar transactino done
                prevtranstime = prevledger[0][3]
                if prevtranstime == currtime:
                    # fetch transaction record
                    frmtrans = query_db("Fetching ledger","SELECT * FROM TRANSACTIONS WHERE TRANSID = "+str(prevledger[0][1]))
                    # this mean transaction done in same minute
                    # fetch the to trans id and match account numbers to current transfer
                    totrans = query_db("Fetching ledger","SELECT * FROM TRANSACTIONS WHERE TRANSID = "+str(prevledger[0][2]))
                    if frmtrans[0][1] == fromacc and totrans[0][1] == toacc:
                        raise ValidationException("Similar transactino done within 1 minute!")

            # we transfer from reserve to account
            # we create debit transaction on reserve
            # deduct from reserve
            stmt = 'INSERT INTO TRANSACTIONS (ACCOUNTID,AMOUNT,TRANSACTIONTYPE) VALUES(?,?,?)'
            values = [(fromacc,amt,"DEBIT")]
            debitid = executemanydefault("debit transaction",stmt,values)
            stmt = 'INSERT INTO TRANSACTIONS (ACCOUNTID,AMOUNT,TRANSACTIONTYPE) VALUES(?,?,?)'
            values = [(toacc,amt,"CREDIT")]
            creditid = executemanydefault("credit transaction",stmt,values)
            # we create new ledger
            stmt = 'INSERT INTO LEDGER (FROMTRANSID,TOTRANSID,STAMP) VALUES(?,?,?)'
            values = [(debitid,creditid,currtime)]
            uid = executemanydefault("ledger addition",stmt,values)
            #update account id reserve
            stmt = "UPDATE ACCOUNTS SET BALANCE = ? WHERE ACCOUNTID = ?"
            values = [(from_acc_bal, fromacc)]
            executemanydefault("account update receiver",stmt,values)
            stmt = "UPDATE ACCOUNTS SET LASTTRANSACTIONID = ? WHERE ACCOUNTID = ?"
            values = [(uid, fromacc)]
            executemanydefault("account transaction id from",stmt,values)
            #update account id
            stmt = "UPDATE ACCOUNTS SET BALANCE = ? WHERE ACCOUNTID = ?"
            values = [(to_acc_bal, toacc)]
            executemanydefault("account update receiver",stmt,values)
            stmt = "UPDATE ACCOUNTS SET LASTTRANSACTIONID = ? WHERE ACCOUNTID = ?"
            values = [(uid, toacc)]
            executemanydefault("account transaction id to",stmt,values)

            # no exceptions all commands will commit after this lets send success
            response = JSONResponse('success')
            response.SetTransferResponse(fromacc,toacc,uid,from_acc_bal,to_acc_bal,currtime,amt)

    except sqlite3.OperationalError as err:
        abort(400, str(err))
    except sqlite3.IntegrityError as err:
        abort(400, str(err))
    except ValidationException as err:
        abort(400, str(err))

    return response

# sanity
def SANITY():
    conn = get_db()

    logging.debug("%s: checking SANITY",__name__)
    
    try:
        with conn:  # manages transactino or all rollbacks!
            debits = query_db("Fetching all debit transactions","SELECT * FROM TRANSACTIONS WHERE TRANSACTIONTYPE = \"DEBIT\"")
            credits = query_db("Fetching all credit transactions","SELECT * FROM TRANSACTIONS WHERE TRANSACTIONTYPE = \"CREDIT\"")
            debitsum = 0
            creditsum = 0
            for credit in credits:
                creditsum = creditsum+credits[0][2]
            for debit in debits:
                debitsum = debitsum+debits[0][2]

            if debitsum != creditsum:
                raise ValidationException("ERROR: Bank reserve Insane!")

            response = JSONResponse('success','Bank reserve Sane')

    except sqlite3.OperationalError as err:
        abort(400, str(err))
    except sqlite3.IntegrityError as err:
        abort(400, str(err))
    except ValidationException as err:
        abort(400, str(err))

    return response












##############################################################################################
####TODO: seperate fil#################   JSON REPONSE      #######################################
##############################################################################################
# 1{
# 2 "id": "transaction_id",
# 3 "from":{
# 4 "id": "account_no",
# 5 "balance": "current_balance"
# 6 },
# 7 "to":{
# 8 "id": "account_no",
# 9 "balance": "current_balance"
# 10 },
# 11 "transfered": "transfer_amount"
# 12 "created_datetime": "transaction created time"
# 13}
import json
from json import JSONEncoder

class JSONResponse:
    def __init__(self,status,message=None):
        self.status = status
        self.message = message
    
    def SetTransferResponse(self,frm,to,uid,frmbal,tobal,time, amt):
        data = {}
        data['id'] = uid
        data['from'] = {}
        data['from']['id'] = frm
        data['from']['balance'] = frmbal
        
        data['to'] = {}
        data['to']['id'] = to
        data['to']['balance'] = tobal

        data['transfered'] = amt
        data['created_datetime'] = time

        self.message = data

    def GenerateJSON(self):
        return json.dumps(self, indent=4, cls=JSONResponseEncoder)
    
    
    def GenerateJSONDict(self):
        data = {}
        data['status'] = self.status
        data['message'] = self.message
        return data

# subclass JSONEncoder
class JSONResponseEncoder(JSONEncoder):
        def default(self, o):
            return o.__dict__

















##############################################################################################
##################################   FLASK APIs        #######################################
##############################################################################################


# runs everytime when the response context is cleared
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.errorhandler(400)
def custom400(error):
    response = JSONResponse('failure',error.description)
    return response.GenerateJSON()

@app.route("/init/<int:totalreserve>/<int:accounts>", methods=['POST'])
def init(totalreserve,accounts):
    logging.debug('init: initing DB and creating tables')
    # TODO: fetch values from headers
    # 1. create the DB from scratch
    try:
        init_db()
    except sqlite3.OperationalError as err:
        abort(400, 'Unable to create DB:'+str(err))
    except sqlite3.IntegrityError as err:
        abort(400, 'Unable to create DB:'+str(err))


    # 2. create new account with 1 id with reserve money
    stmt = 'INSERT INTO ACCOUNTS VALUES(?,?,?,?)'
    values = [(0,"reserve",totalreserve,0)]
    executemanydata("Creating bank",stmt,values)


    # 3. run a loop to number of accounts and add 0 money
    logging.debug("init: adding default account and first transaction for %d ",totalreserve)
    stmt = 'INSERT INTO ACCOUNTS VALUES(?,?,?,?)'
    values = []
    for x in range(accounts):
        values.append((1000+x,"name_"+str(x),0,0))
    executemanydata("adding accounts",stmt,values)

    # 4. transfer the money from reserve to all accounts in loop
    # this should fill transaction table as well as common table
    # get per account money, this is so that no new money from
    # thin air
    peracc = totalreserve // accounts
    logging.debug("init: creating %d accounts with %d balance",accounts,peracc)

    res = query_db("Fetching accounts","SELECT * FROM ACCOUNTS")
    for x in res:
        if x[0] != 0:
            fromacc = 0
            toacc = x[0]
            TRANSFER(fromacc,toacc,peracc)

    # 5. fetch all account ids with current balance and return
    logging.debug("init: returning all account ids created")
    res = query_db("Fetching accounts","SELECT * FROM ACCOUNTS")
    values = []
    for x in res:
        values.append({"account_no":x[0],"balance":x[2],"name":x[1]})

    # 6. generate a response
    response = JSONResponse('success',values)

    return jsonify(response.GenerateJSONDict())



# transfer atomically
@app.route("/transfer/<int:from_acc>/<int:to_acc>/<int:amount>", methods=['POST'])
def transfer(from_acc,to_acc,amount):
    # TODO: fetch values from headers

    response = TRANSFER(from_acc,to_acc,amount)

    return jsonify(response.GenerateJSONDict())


@app.route("/statement/<int:account>", methods=['GET', 'POST'])
def statement(account):
    # TODO: fetch values from headers
    logging.debug('%s: validating if account is valid',__name__)
    logging.debug('%s: fetching balance for %d from accounts table',__name__,account)
    logging.debug('%s: fetching all the transactions for this account',__name__)

    return {
        "status": "Success"
    }

@app.route("/sanity", methods=['GET'])
def sanity():
    # TODO: fetch values from headers    
    # whatever be the case, no new money should be present
    # so the debits must be equal to credits
    logging.debug("checking sanity")
    response = SANITY()

    return jsonify(response.GenerateJSONDict())

# print("running on 5000")
serve(app, listen='*:5000')
