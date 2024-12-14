import requests
import json
import jsonpath

def test_oAuth_API():
    token_url="https://thetestingworldapi.com/Token"
    data={'grant_type':'password','username':'admin','password':'adminpass'}
    response=requests.post(token_url,data)
    token_value=jsonpath.jsonpath(response.json(),'access_token')
    auth={'Authorization':'Bearer '+token_value[0]}
    API_URL="https://thetestingworldapi.com/api/StDetails/1104"
    response=requests.get(API_URL,headers=auth)
    print(response.text)