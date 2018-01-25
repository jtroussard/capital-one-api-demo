#!/usr/bin/python3

"""Capital One Api Demo

Capital One Api Tutorial: http://api.reimaginebanking.com. Small demo 
expirementing with Capital One's Api.

Copyright (C) 2018 Jacques Troussard

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or any 
later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
Author can be contacted at, tekksparrows@gmail.com
"""

import json
import requests
from config.config import *

__author__     = "Jacques Troussard"
__date__       = "01/24/2018"
__email__      = "tekksparrows@gmail.com"

# endpoint pieces
url = "http://api.reimaginebanking.com/"
cust_url = "customers/"
acct_url = "accounts/"
key_url = "?key={}".format(API_KEY)

# build customer list request
req_url = url + cust_url + key_url
response = requests.get(req_url)
try:
    response.raise_for_status
    r_cust = response.json()
except Exception as err:
    print("\t{}:\n{}".format(type(err), err))

#build accounts list for each customer and record networth
cust_networth_dict = {}
for customer in r_cust:
    cust_url = "customers/{}/".format(customer['_id'])
    req_url = url + cust_url + acct_url + key_url
    response = requests.get(req_url)
    try:
        response.raise_for_status
        r_acct = response.json()
    except Exception as err:
        print("\t{}:\n{}".format(type(err), err))
    networth = 0
    for doc in r_acct:
        networth += doc['balance']
    full_name = "{} {}".format(customer['first_name'], customer['last_name'])
    new_entry = {'full_name': full_name, 'networth': networth}
    cust_networth_dict[customer['_id']] = new_entry

# loop through resulting data and print to screen
for key in cust_networth_dict:
    print("{}'s net worth is {}".format(cust_networth_dict[key]['full_name'], cust_networth_dict[key]['networth']))