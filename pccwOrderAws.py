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
if len(sys.argv) != 6:
  print("""ERROR: script expects five arguments for:
  srcPortId
  awsAccountNumber
  awsConnectionName
  awsConnectionName
  speed
  """)
  exit()
#
# Order an AWS Direct Connect
#
url = 'https://api.consoleconnect.com/api/company/eurovisionservices/connections/directConnectPartner/AWS/layer2'
body = {
  "destUsername": "amazon",
  "type": "LAYER2",
  "name": sys.argv[3],
  "srcPortId": sys.argv[1],
  "destPortId": "5aa730f8efe3bc00124d0766",
  "speed": int(sys.argv[5]),
  "paymentType": sys.argv[4],
  "partner": {
    "account": sys.argv[2]
  }
}
#print(json.dumps(body))
res = requests.put(url, data=json.dumps(body), headers = auth)
response = json.loads(res.content.decode('utf-8'))
print(yaml.dump(response))
