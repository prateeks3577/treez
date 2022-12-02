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
