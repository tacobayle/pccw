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
# Retrieve AWS Region, Cities, Ids
response = pccwMain.ppcwGetAwsRegion(auth)
listAwsRegion = []
listAwsRegionId = []
for item in response['results']:
  dictAwsRegion = {}
  dictAwsRegion['region'] = item['partner']['regionNames'][0]
  dictAwsRegion['id'] = item['id']
  dictAwsRegion['city'] = item['metro']['name']
  listAwsRegionId.append(item['id'])
  listAwsRegion.append(dictAwsRegion)



  # dictAwsRegion[item['partner']['regionNames'][0]] = item['id']
  # # listAwsRegion.append(item['partner']['regionNames'][0])
  # # listAwsCity.append(item['metro']['name'])
  # # listAwsRegionId.append(item['id'])
print(listAwsRegion)
print(listAwsRegionId)
