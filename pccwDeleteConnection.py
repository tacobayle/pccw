import json, requests, os, sys, yaml
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
if len(sys.argv) != 2:
  print('ERROR: script expects one argument for connection id')
  exit()
#
# Delete Connection
#
response = pccwMain.ppcwDeleteConnection(os.environ['PCCWCOMPANY'], auth, sys.argv[1])
print(yaml.dump(response))
