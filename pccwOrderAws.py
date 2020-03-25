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
if len(sys.argv) != 8:
  print("""ERROR: script expects seven arguments for:
  awsConnectionName
  srcPortId
  destPortId
  speed
  paymentType
  awsAccountNumber
  AmountOfDays
  """)
  exit()
#
# Retrieve PCCW ports
#
listPccwPort, listPccwPortId = pccwMain.ppcwReadPortId(os.environ['PCCWCOMPANY'], auth)
#
# retrieve AWS regions, Ids, Cities
#
listAwsRegion, listAwsRegionId = pccwMain.ppcwGetAwsRegion(auth)
#
# check if AWS src port is correct
#
if sys.argv[2] not in listPccwPortId:
  print('please choose one of the following Ports Ids')
  print(yaml.dump(listPccwPort))
  exit()
#
# check if AWS region id is correct
#
if sys.argv[3] not in listAwsRegionId:
  print('please choose one of the following ids')
  print(yaml.dump(listAwsRegion))
  exit()
#
# Order an AWS Direct Connect
#
# data tested successfuly: body1 = """{"srcPortId": "5e429ef0d6b9a000166c3b65", "destPortId": "5b456eda852dad001a8cf2cd" , "srcVlanRequest": null, "speed": 500, "name": "AWS Direct Connect", "type": "LAYER2", "partner": {"account": "265034252711"}, "regionId": "5a80c78c1347a30012dd1c53","destRegionId": "5a80c78c1347a30012dd1c53", "duration": 1, "durationUnit": "d", "evergreen": false, "paymentType": "invoice"}"""
#
url = 'https://api.consoleconnect.com/api/company/' + os.environ['PCCWCOMPANY'] + '/connections/directConnectPartner/AWS/layer2'
body = {
  "type": "LAYER2",
  "name": sys.argv[1],
  "srcPortId": sys.argv[2],
  "destPortId": sys.argv[3],
  "speed": int(sys.argv[4]),
  "paymentType": sys.argv[5],
  "partner": {
    "account": sys.argv[6]
  },
  "duration": int(sys.argv[7]),
  "durationUnit": "d"
}
res = requests.put(url, data=json.dumps(body), headers = auth)
response = json.loads(res.content.decode('utf-8'))
#print(response)
idPccw = response['id']
#
# Wait for Service to be PENDING_ACCEPTANCE
#
while True:
  response = pccwMain.ppcwReadConnection(os.environ['PCCWCOMPANY'], auth, idPccw)
  if response['status'] == 'PENDING_ACCEPTANCE':
      break
  time.sleep(15)
response = pccwMain.ppcwReadConnection(os.environ['PCCWCOMPANY'], auth, idPccw)
#
# Output the parameters in the console
#
print(str(response['srcTag']) + ';' + str(response['destTag']) + ';' + str(response['partner']['connectionId']))
#
# Output the parameters in a yaml file
#
output = {}
output['id'] = str(idPccw)
output['srcTag'] = str(response['srcTag'])
output['destTag'] = str(response['destTag'])
output['partnerConnectionId'] = str(response['partner']['connectionId'])
with open('pccwOrderAws.yml', 'w') as file:
  yaml.dump(output, file, default_flow_style=False)
