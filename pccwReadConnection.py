import json, requests, os, sys, yaml
import pccwMain
#
# PCCW credential needs to be set as env variables
#
# export PCCWLOGIN=abcdef
# export PCCWPASS=abcdef
#
# retrieve API token
auth = pccwMain.pccwGetToken(os.environ['PCCWLOGIN'], os.environ['PCCWPASS'])
#
if len(sys.argv) != 2:
  print('ERROR: script expects one argument for connection id')
  exit()
connectionId = sys.argv[1]
#
# Read Connection
#
url = 'https://api.consoleconnect.com/api/company/eurovisionservices/connections/' + str(connectionId)
res = requests.get(url, headers = auth)
response = json.loads(res.content.decode('utf-8'))
print(yaml.dump(response))
