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

# init db
print("initing db")
r = requests.post('http://127.0.0.1:5000/init/4000/5')
print(r.text)

print(" test basic - transact")
r = requests.post('http://127.0.0.1:5000/transfer/1001/1002/100')
print(r.text)

print(" test low balance - transact")
r = requests.post('http://127.0.0.1:5000/transfer/1001/1002/900')
print(r.text)

print(" test transaction too soon - transact")
r = requests.post('http://127.0.0.1:5000/transfer/1001/1002/100')
print(r.text)


# print("statement")
# r = requests.post('http://127.0.0.1:5000/statement/1')
# print(r.text)

print("test sanity")
r = requests.get('http://127.0.0.1:5000/sanity')
print(r.text)


