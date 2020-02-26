import json
import requests
import os
import sys
import yaml
#
# PCCW credential needs to be set as env variables
#
# export PCCWLOGIN=abcdef
# export PCCWPASS=abcdef
# 
if len(sys.argv) != 2:
  print('ERROR: script expects one argument for connection id')
  exit()
connectionId = sys.argv[1]
url = 'https://api.consoleconnect.com/api/auth/token'
payload = {}
payload['email'] = os.environ['PCCWLOGIN']
payload['password'] = os.environ['PCCWPASS']
res = requests.put(url, data = payload)
response = json.loads(res.content.decode('utf-8'))
auth = {}
auth['portal-token'] = response['token']
#
# Read Connection
#
url = 'https://api.consoleconnect.com/api/company/eurovisionservices/connections/' + str(connectionId)
res = requests.get(url, headers = auth)
response = json.loads(res.content.decode('utf-8'))
print(yaml.dump(response))
