import json, requests, os, sys, yaml, time
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
# data tested: {"srcPortId":"5e429ef0d6b9a000166c3b65","destPortId":"5b456eda852dad001a8cf2cd","srcVlanRequest":null,"speed":500,"name":"AWS Direct Connect","type":"LAYER2","partner":{"account":"265034252711"},"regionId":"5a80c78c1347a30012dd1c53","destRegionId":"5a80c78c1347a30012dd1c53","duration":1,"durationUnit":"d","evergreen":false,"paymentType":"invoice"}
#
url = 'https://api.consoleconnect.com/api/company/eurovisionservices/connections/directConnectPartner/AWS/layer2'
#  "destUsername": "amazon",
body = {
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
body1 = """{"srcPortId": "5e429ef0d6b9a000166c3b65", "destPortId": "5b456eda852dad001a8cf2cd" , "srcVlanRequest": null, "speed": 500, "name": "AWS Direct Connect", "type": "LAYER2", "partner": {"account": "265034252711"}, "regionId": "5a80c78c1347a30012dd1c53","destRegionId": "5a80c78c1347a30012dd1c53", "duration": 1, "durationUnit": "d", "evergreen": false, "paymentType": "invoice"}"""
#print(json.dumps(body))
#print(auth)
#print(body1)
#res = requests.put(url, data=json.dumps(body), headers = auth)
res = requests.put(url, data=body1, headers = auth)
response = json.loads(res.content.decode('utf-8'))
idPccw = response['id']
while True:
  response = pccwMain.ppcwReadConnection(os.environ['PCCWCOMPANY'], auth, idPccw)
  #print(response['status'])
  if response['status'] == 'PENDING_ACCEPTANCE':
      break
  time.sleep(15)
response = pccwMain.ppcwReadConnection(os.environ['PCCWCOMPANY'], auth, idPccw)
print(str(response['srcTag']) + ';' + str(response['destTag']) + ';' + str(response['partner']['connectionId']))
