import json, requests, os
import pccwMain
#
# PCCW credential needs to be set as env variables
#
# export PCCWLOGIN=abcdef
# export PCCWPASS=abcdef
# export PCCWCOMPANY=abcdef
#
# retrieve API token
auth = pccwMain.pccwGetToken(os.environ['PCCWLOGIN'], os.environ['PCCWPASS'])
#
# List ports
#
response = pccwMain.ppcwReadPort(os.environ['PCCWCOMPANY'], auth)
#
# pretty print response
#
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
      print('\t\t--')
  print('\t----')
