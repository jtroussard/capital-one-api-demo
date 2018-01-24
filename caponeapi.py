import json
import requests
from config.config import *

# endpoint pieces
url = "http://api.reimaginebanking.com/"
cust_url = "customers/{}/".format(CUST_ID)
acct_url = "accounts/"
key_url = "?key={}".format(API_KEY)

# build customer request
req_url = url + cust_url + key_url
response = requests.get(req_url)
if response.status_code == requests.codes.ok:
    r_cust = response.json()
    full_name = "{} {}".format(r_cust['first_name'], r_cust['last_name'])

#build accounts request
req_url = url + cust_url + acct_url + key_url
response = requests.get(req_url)
if response.status_code == requests.codes.ok:
    r_acct = response.json()

networth = 0
for doc in r_acct:
    networth += doc['balance']

print("{}'s net worth is {}".format(full_name, networth))