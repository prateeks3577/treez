# this client initializes the bank accounts
# verifies expected response is received
# 1. gives option to init the DB
# - asks for total money in bank
# - asks for number of accounts
# - asks for initial amount
# 2. test transaction 
# - asks for from
# - asks for to account
# - money
# 3. test sanity of DB
# 4. performance test , responds failed cases and sanity
# - asks for number of random transactions
# - asks for number of workers

import requests
import json



# print(" test low balance - transact")
# r = requests.post('http://127.0.0.1:5000/transfer/1001/1002/900')
# print(r.text)

# print(" test transaction too soon - transact")
# r = requests.post('http://127.0.0.1:5000/transfer/1001/1002/100')
# print(r.text)


# print("statement")
# r = requests.post('http://127.0.0.1:5000/statement/1')
# print(r.text)

# print("test sanity")
# r = requests.get('http://127.0.0.1:5000/sanity')
# print(r.text)

fromacc = []
tocc = []
transten = 0
transfifty = 0

while True:
    print("######################################")
    print("1. Init DB")
    print("2. Do 10 transactions")
    print("3. Do 500 transactions")
    print("4. sanity check")
    print("5. statement")
    
    inp = input(" enter yuo choice or q to quit - ")
    print("you entered - ",inp)

    if int(inp) == 1:
        # init db
        print("initing db")
        money = input(" total amt in bank - ")
        accs =  input(" number of accounts - ")
        r = requests.post('http://127.0.0.1:5000/init/'+money+'/'+accs)
        data = json.loads(r.text)
        for x in data['message']:
            print(x)
            if x['account_no'] > 0 and x['account_no']%2 > 0:
                fromacc.append(x['account_no'])
            elif x['account_no'] > 0 and x['account_no']%2 == 0:
                tocc.append(x['account_no'])

        transten = int(money) / int(accs)
        transten = int(transten) // 10

        transfifty = int(money)/int(accs)
        transfifty = int(transten)//50

    if int(inp) == 2:
        fail = 0
        for x in range(10):
            print(" test basic - transact")
            index = x%len(fromacc)
            print('http://127.0.0.1:5000/transfer/'+str(fromacc[index])+'/'+str(tocc[index])+'/'+str(transten))
            r = requests.post('http://127.0.0.1:5000/transfer/'+str(fromacc[index])+'/'+str(tocc[index])+'/'+str(transten))
            print(r.text)
            data = json.loads(r.text)
            if data['status'] == 'failure':
                fail = fail + 1
        
        print("total failed - ",fail)


    if int(inp) == 3:
        fail = 0
        for x in range(50):
            print(" test basic - transact")
            index = x%len(fromacc)
            print('http://127.0.0.1:5000/transfer/'+str(fromacc[index])+'/'+str(tocc[index])+'/'+str(transfifty))
            r = requests.post('http://127.0.0.1:5000/transfer/'+str(fromacc[index])+'/'+str(tocc[index])+'/'+str(transfifty))
            print(r.text)
            data = json.loads(r.text)
            if data['status'] == 'failure':
                fail = fail + 1
        
        print("total failed - ",fail)


    if int(inp) == 4:
        print("sanity")
        r = requests.get('http://127.0.0.1:5000/sanity')
        print(r.text)
    
    if int(inp) == 5:
        print("statement")
        acc = input("enter account no - ")
        r = requests.get('http://127.0.0.1:5000/statement/'+acc)
        print(r.text)
    


