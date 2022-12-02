# treez
# Table of contents
1. [How to use?](#howtouse)
3. [Request APIs](#paragraph2) - [init](#subparagraph21), [transfer](#subparagraph22), [sanity](#subparagraph23), [statement](#subparagraph24)
4. [Response](#pararaph3) - [success](#subparagraph31), [error](#subparagraph32)
5. [Database Model](#paragraph1)
6. [Design Considerations](#paragraph6)
7. [Files](#paragraph7)

## How to use? <a name="howtouse"></a>
### Prerequisites
- can run only on windows
- python 3.9 should be installed
### Steps
- run startserver.bat as administrator, this will install all necesary packages and start flask which will run on port 127.0.0.1:5000
- run startclient.bat as administrator, this will run one client and some test cases, can always check DB sanity by running different options


C:\PROJECT\treez-main\treez-main>echo hello
hello

C:\PROJECT\treez-main\treez-main>py -m pip install --upgrade pip
Requirement already satisfied: pip in c:\users\ssure\appdata\local\programs\python\python311\lib\site-packages (22.3.1)

C:\PROJECT\treez-main\treez-main>py -m pip install --user virtualenv
Requirement already satisfied: virtualenv in c:\users\ssure\appdata\roaming\python\python311\site-packages (20.17.0)
Requirement already satisfied: distlib<1,>=0.3.6 in c:\users\ssure\appdata\roaming\python\python311\site-packages (from virtualenv) (0.3.6)
Requirement already satisfied: filelock<4,>=3.4.1 in c:\users\ssure\appdata\roaming\python\python311\site-packages (from virtualenv) (3.8.0)
Requirement already satisfied: platformdirs<3,>=2.4 in c:\users\ssure\appdata\roaming\python\python311\site-packages (from virtualenv) (2.5.4)

C:\PROJECT\treez-main\treez-main>py -m venv env
Error: [Errno 13] Permission denied: 'C:\\PROJECT\\treez-main\\treez-main\\env\\Scripts\\python.exe'

C:\PROJECT\treez-main\treez-main>CALL env\Scripts\activate
Requirement already satisfied: Flask in c:\project\treez-main\treez-main\env\lib\site-packages (2.2.2)
Requirement already satisfied: Werkzeug>=2.2.2 in c:\project\treez-main\treez-main\env\lib\site-packages (from Flask) (2.2.2)
Requirement already satisfied: Jinja2>=3.0 in c:\project\treez-main\treez-main\env\lib\site-packages (from Flask) (3.1.2)
Requirement already satisfied: itsdangerous>=2.0 in c:\project\treez-main\treez-main\env\lib\site-packages (from Flask) (2.1.2)
Requirement already satisfied: click>=8.0 in c:\project\treez-main\treez-main\env\lib\site-packages (from Flask) (8.1.3)
Requirement already satisfied: colorama in c:\project\treez-main\treez-main\env\lib\site-packages (from click>=8.0->Flask) (0.4.6)
Requirement already satisfied: MarkupSafe>=2.0 in c:\project\treez-main\treez-main\env\lib\site-packages (from Jinja2>=3.0->Flask) (2.1.1)
Requirement already satisfied: waitress in c:\project\treez-main\treez-main\env\lib\site-packages (2.1.2)
Requirement already satisfied: requests in c:\project\treez-main\treez-main\env\lib\site-packages (2.28.1)
Requirement already satisfied: charset-normalizer<3,>=2 in c:\project\treez-main\treez-main\env\lib\site-packages (from requests) (2.1.1)
Requirement already satisfied: idna<4,>=2.5 in c:\project\treez-main\treez-main\env\lib\site-packages (from requests) (3.4)
Requirement already satisfied: urllib3<1.27,>=1.21.1 in c:\project\treez-main\treez-main\env\lib\site-packages (from requests) (1.26.13)
Requirement already satisfied: certifi>=2017.4.17 in c:\project\treez-main\treez-main\env\lib\site-packages (from requests) (2022.9.24)
######################################
1. Init DB
2. Do 10 transactions
3. Do 500 transactions
4. sanity check
5. statement
 enter yuo choice or q to quit - 1
you entered -  1
initing db
 total amt in bank - 5000
 number of accounts - 50
{'account_no': 0, 'balance': 0, 'name': 'reserve'}
{'account_no': 1000, 'balance': 100, 'name': 'name_0'}
{'account_no': 1001, 'balance': 100, 'name': 'name_1'}
{'account_no': 1002, 'balance': 100, 'name': 'name_2'}
{'account_no': 1003, 'balance': 100, 'name': 'name_3'}
{'account_no': 1004, 'balance': 100, 'name': 'name_4'}
{'account_no': 1005, 'balance': 100, 'name': 'name_5'}
{'account_no': 1006, 'balance': 100, 'name': 'name_6'}
{'account_no': 1007, 'balance': 100, 'name': 'name_7'}
{'account_no': 1008, 'balance': 100, 'name': 'name_8'}
{'account_no': 1009, 'balance': 100, 'name': 'name_9'}
{'account_no': 1010, 'balance': 100, 'name': 'name_10'}
{'account_no': 1011, 'balance': 100, 'name': 'name_11'}
{'account_no': 1012, 'balance': 100, 'name': 'name_12'}
{'account_no': 1013, 'balance': 100, 'name': 'name_13'}
{'account_no': 1014, 'balance': 100, 'name': 'name_14'}
{'account_no': 1015, 'balance': 100, 'name': 'name_15'}
{'account_no': 1016, 'balance': 100, 'name': 'name_16'}
{'account_no': 1017, 'balance': 100, 'name': 'name_17'}
{'account_no': 1018, 'balance': 100, 'name': 'name_18'}
{'account_no': 1019, 'balance': 100, 'name': 'name_19'}
{'account_no': 1020, 'balance': 100, 'name': 'name_20'}
{'account_no': 1021, 'balance': 100, 'name': 'name_21'}
{'account_no': 1022, 'balance': 100, 'name': 'name_22'}
{'account_no': 1023, 'balance': 100, 'name': 'name_23'}
{'account_no': 1024, 'balance': 100, 'name': 'name_24'}
{'account_no': 1025, 'balance': 100, 'name': 'name_25'}
{'account_no': 1026, 'balance': 100, 'name': 'name_26'}
{'account_no': 1027, 'balance': 100, 'name': 'name_27'}
{'account_no': 1028, 'balance': 100, 'name': 'name_28'}
{'account_no': 1029, 'balance': 100, 'name': 'name_29'}
{'account_no': 1030, 'balance': 100, 'name': 'name_30'}
{'account_no': 1031, 'balance': 100, 'name': 'name_31'}
{'account_no': 1032, 'balance': 100, 'name': 'name_32'}
{'account_no': 1033, 'balance': 100, 'name': 'name_33'}
{'account_no': 1034, 'balance': 100, 'name': 'name_34'}
{'account_no': 1035, 'balance': 100, 'name': 'name_35'}
{'account_no': 1036, 'balance': 100, 'name': 'name_36'}
{'account_no': 1037, 'balance': 100, 'name': 'name_37'}
{'account_no': 1038, 'balance': 100, 'name': 'name_38'}
{'account_no': 1039, 'balance': 100, 'name': 'name_39'}
{'account_no': 1040, 'balance': 100, 'name': 'name_40'}
{'account_no': 1041, 'balance': 100, 'name': 'name_41'}
{'account_no': 1042, 'balance': 100, 'name': 'name_42'}
{'account_no': 1043, 'balance': 100, 'name': 'name_43'}
{'account_no': 1044, 'balance': 100, 'name': 'name_44'}
{'account_no': 1045, 'balance': 100, 'name': 'name_45'}
{'account_no': 1046, 'balance': 100, 'name': 'name_46'}
{'account_no': 1047, 'balance': 100, 'name': 'name_47'}
{'account_no': 1048, 'balance': 100, 'name': 'name_48'}
{'account_no': 1049, 'balance': 100, 'name': 'name_49'}
######################################
1. Init DB
2. Do 10 transactions
3. Do 500 transactions
4. sanity check
5. statement
 enter yuo choice or q to quit - 2
you entered -  2
 test basic - transact
http://127.0.0.1:5000/transfer/1001/1000/10
{"message":{"created_datetime":"2022-12-02 09:17:27","from":{"balance":90,"id":1001},"id":51,"to":{"balance":110,"id":1000},"transfered":10},"status":"success"}

 test basic - transact
http://127.0.0.1:5000/transfer/1003/1002/10
{"message":{"created_datetime":"2022-12-02 09:17:27","from":{"balance":90,"id":1003},"id":52,"to":{"balance":110,"id":1002},"transfered":10},"status":"success"}

 test basic - transact
http://127.0.0.1:5000/transfer/1005/1004/10
{"message":{"created_datetime":"2022-12-02 09:17:27","from":{"balance":90,"id":1005},"id":53,"to":{"balance":110,"id":1004},"transfered":10},"status":"success"}

 test basic - transact
http://127.0.0.1:5000/transfer/1007/1006/10
{"message":{"created_datetime":"2022-12-02 09:17:27","from":{"balance":90,"id":1007},"id":54,"to":{"balance":110,"id":1006},"transfered":10},"status":"success"}

 test basic - transact
http://127.0.0.1:5000/transfer/1009/1008/10
{"message":{"created_datetime":"2022-12-02 09:17:27","from":{"balance":90,"id":1009},"id":55,"to":{"balance":110,"id":1008},"transfered":10},"status":"success"}

 test basic - transact
http://127.0.0.1:5000/transfer/1011/1010/10
{"message":{"created_datetime":"2022-12-02 09:17:27","from":{"balance":90,"id":1011},"id":56,"to":{"balance":110,"id":1010},"transfered":10},"status":"success"}

 test basic - transact
http://127.0.0.1:5000/transfer/1013/1012/10
{"message":{"created_datetime":"2022-12-02 09:17:27","from":{"balance":90,"id":1013},"id":57,"to":{"balance":110,"id":1012},"transfered":10},"status":"success"}

 test basic - transact
http://127.0.0.1:5000/transfer/1015/1014/10
{"message":{"created_datetime":"2022-12-02 09:17:27","from":{"balance":90,"id":1015},"id":58,"to":{"balance":110,"id":1014},"transfered":10},"status":"success"}

 test basic - transact
http://127.0.0.1:5000/transfer/1017/1016/10
{"message":{"created_datetime":"2022-12-02 09:17:27","from":{"balance":90,"id":1017},"id":59,"to":{"balance":110,"id":1016},"transfered":10},"status":"success"}

 test basic - transact
http://127.0.0.1:5000/transfer/1019/1018/10
{"message":{"created_datetime":"2022-12-02 09:17:27","from":{"balance":90,"id":1019},"id":60,"to":{"balance":110,"id":1018},"transfered":10},"status":"success"}

total failed -  0
######################################
1. Init DB
2. Do 10 transactions
3. Do 500 transactions
4. sanity check
5. statement
 enter yuo choice or q to quit - 4
you entered -  4
sanity
{"message":"Bank reserve Sane","status":"success"}

######################################
1. Init DB
2. Do 10 transactions
3. Do 500 transactions
4. sanity check
5. statement
 enter yuo choice or q to quit - 5
you entered -  5
statement
enter account no - 1001
{"message":[{"amount":100,"transid":4,"type":"CREDIT"},{"amount":10,"transid":101,"type":"DEBIT"}],"status":"success2"}

######################################
1. Init DB
2. Do 10 transactions
3. Do 500 transactions
4. sanity check
5. statement
 enter yuo choice or q to quit -


## APIs <a name="paragraph2"></a>
Total four APIs, this is minimal and below is description of each
### /init/reserve/no_of_accounts <a name="subparagraph21"></a>
- This API creates runs schema.sql.
- Inserts first account entry for reserve with initial money
- creates the number of accounts, 
- transfers eqally all the money to these accounts from reserve. 
- **Returns** list of accounts with there balance.
### /transfer/from/to/amount <a name="subparagraph22"></a>
- Below operations done in sqlite3 session i.e. if any fails all rolls back
- This API validates from and to are valid account id. 
- Validates from has sufficient balance
- verifies the same transactino is not being done within 1 minute
- creates two entries in TRANSACTIONS table for credit and debit
- creates single entry on LEDGER with timestamp
- updates balance on account table 
### /sanity <a name="subparagraph23"></a>
- runs a loop for all credits on TRANSACTIONS table and similarly for debits
- matches to verify DB is in right condition no new money ended
### /statement/account <a name="subparagraph24"></a>
- just statement

## Response <a name="pararaph3"></a>
Standard JSON for responses such that the common JSON structure to respond success or failure
{
    "status": "success/failure",
    "message": "custom message for failure and JSON for success"
}
Client must verify the value of status as success or failure
### success response <a name="subparagraph31"></a>
- for transfer goes similar to the one mentinoed in assignment but encapsulated in common status, message
- {"message":{"created_datetime":"2022-12-02 03:28:31","from":{"balance":700,"id":1001},"id":6,"to":{"balance":900,"id":1002},"transfered":100},"status":"success"}
### failure response <a name="subparagraph32"></a>
- this is driven by different exceptions accross code. Whenever any exception occurs in a transaction, the changes are rolledback and the status set to failure and message as required
- {
    "status": "failure",
    "message": "Similar transactino done within 1 minute!"
}

## Database Model <a name="paragraph1"></a>
As per assignment , some changes have been made to the tables. In total three tables are added to minimize the data repetition and easier bookkeeping.
### TRANSACTIONS 
- two types of transactions are defined CREDIT and DEBIT. This table takes care of keeping one type of transaction for each account. Have removed timestamp from this table and it is a tuple of <TransactionID><AccountID><Aomount><TransactinoType>. The reason for removal was to have generic view of bank, easier for audit
### LEDGER
- this is actual bookkeeping of complete transactions, and contains two transaction id for each account direction also keeps the transaction time
### ACCOUNTS
- this is to keep record of all the accounts in bank. It has one default account with id 0 which stores the actual money in bank. On creation in init API new accounts can be made and transactions are made from this reserve account to other. This is to make sure no money is created from thin air and this way we can audit the bank. Also to use the transfer api

## Design Considerations <a name="paragraph6"></a>
### What happens under high concurrency?
- In this design we are reliant on sqlite3 internal handling of concurrency. As per documents if two process try to change the DB simultaneously SQLITE_BUSY Operational exception is thrown. Usually getting this is very rare as connect method waits for 5 seconds before this exception occuring. In current design one request will fail. 
- To fix this we can increase the number of seconds connect waits to get connection to DB. 
- To maintain concurrency here the DB has to come in picture and maintain integrity. Since all the threads/process will have there own cursor so the DB will fail in case some process is updating same values. Can be realized with opening multiple clients and running concurrent transactions.
- in current example timeout is increased to 10 seconds
### What happens if your database becomes unavailable in the middle of your logic?
- in this case an exception will occur on commit and via exception handling status failure will be sent to client
### What happens if 2 users (A, B) transfer money to user C at the same time?
- The DB will take care such that each request is processed one by one as the resource is bottle neck here
### And so forth.
### How do you handle and structure the errors that you return to the client?
- via exception handling


## Files <a name="paragraph7"></a>
debug.log - is used for logging
server.py - contains all server elements
client.py - contains all client implementation
startserver.bat - starts server
startclient.bat - starts client
schema.sql - schema of the database
