import json
import requests
import os
#
# PCCW credential needs to be set as env variables
#
# export PCCWLOGIN=abcdef
# export PCCWPASS=abcdef
# 
url = 'https://api.consoleconnect.com/api/auth/token'
payload = {}
payload['email'] = os.environ['PCCWLOGIN']
payload['password'] = os.environ['PCCWPASS']
res = requests.put(url, data = payload)
response = json.loads(res.content.decode('utf-8'))
auth = {}
auth['portal-token'] = response['token']
#
# List ports
#
url = 'https://api.consoleconnect.com/api/company/eurovisionservices/ports'
res = requests.get(url, headers = auth)
response = json.loads(res.content.decode('utf-8'))
print('List of ports and services associated:')
for port in response['results']:
  print('\tdataCenterFacility username: ' + str(port['dataCenterFacility']['username']))
  print('\tname: ' + str(port['name']))
  print('\tspeed: ' + str(port['speed']['name']))
  print('\tstatus ' + str(port['status']))
  print('\tlinkState ' + str(port['linkState']))
  print('\tid: ' + str(port['id']))
  print('\tcapacity total: ' + str(port['capacity']['total']))
  print('\tcapacity utilised: ' + str(port['capacity']['utilised']))
  print('\tcapacity remaining: ' + str(port['capacity']['remaining']))
  if len(port['connections']) > 0:
    print('\tList of services:')
    for connection in port['connections']:
      print('\t\tname: ' + str(connection['name']))
      print('\t\tid: ' + str(connection['id']))
      print('\t\tspeed: ' + str(connection['speed']))
      print('\t\tstatus: ' + str(connection['status']))
    #url = 'https://api.consoleconnect.com/api/company/eurovisionservices/connections/' + str(connection['id'])
    #res = requests.get(url, headers = auth)
    #response = json.loads(res.content.decode('utf-8'))
    #print(response)
      print('\t\t--')
  print('\t----')
