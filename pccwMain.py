import json
import requests
import os
#
# PCCW credential needs to be set as env variables
#
# export PCCWLOGIN=abcdef
# export PCCWPASS=abcdef
#
def pccwGetToken(username, password):
  # this function queries the API to retrieve the token
    url = 'https://api.consoleconnect.com/api/auth/token'
    payload = {}
    payload['email'] = username
    payload['password'] = password
    res = requests.put(url, data = payload)
    response = json.loads(res.content.decode('utf-8'))
    dict = {}
    dict['portal-token'] = response['token']
    return dict

#
#
#
#
if __name__ == '__main__':
  exit()
