# treez
# Table of contents
1. [How to use?](#howtouse)
3. [Request APIs](#paragraph2)
    3.1. [init](#subparagraph21)
    3.2. [transfer](#subparagraph22)
    3.3. [sanity](#subparagraph23)
    3.4. [statement](#subparagraph24)
4. 
4. [Database Model](#paragraph1)

## How to use? <a name="howtouse"></a>
### Prerequisites
- can run only on windows
- python 3.9 should be installed
### Steps
- run startserver.bat, this will install all necesary packages and start flask which will run on port 127.0.0.1:5000
- run startclient.bat, this will run one client and some test cases, can always check DB sanity by running different options

## APIs <a name="paragraph2"></a>
Total four APIs, this is minimal and below is description of each
### /init/<reserve>/<no_of_accounts> <a name="subparagraph21"></a>
- This API creates runs schema.sql.
- Inserts first account entry for reserve with initial money
- creates the number of accounts, 
- transfers eqally all the money to these accounts from reserve. 
- **Returns** list of accounts with there balance.
### /transfer/<from>/<to>/<amount> <a name="subparagraph22"></a>
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
### /statement/<account> <a name="subparagraph24"></a>
- just statement

## Database Model <a name="paragraph1"></a>
As per assignment , some changes have been made to the tables. In total three tables are added to minimize the data repetition and easier bookkeeping.
###TRANSACTIONS 
- two types of transactions are defined CREDIT and DEBIT. This table takes care of keeping one type of transaction for each account. Have removed timestamp from this table and it is a tuple of <TransactionID><AccountID><Aomount><TransactinoType>. The reason for removal was to have generic view of bank, easier for audit
###LEDGER
- this is actual bookkeeping of complete transactions, and contains two transaction id for each account direction also keeps the transaction time
###ACCOUNTS
- this is to keep record of all the accounts in bank. It has one default account with id 0 which stores the actual money in bank. On creation in init API new accounts can be made and transactions are made from this reserve account to other. This is to make sure no money is created from thin air and this way we can audit the bank. Also to use the transfer api

## Another paragraph <a name="paragraph2"></a>
The second paragraph text
