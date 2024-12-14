import requests
import json
import jsonpath
def test_Add_new_data():
    API_URL="https://thetestingworldapi.com/api/studentsDetails"
    f=open('C:/Users/akhila.polasu/LERANpythonbasics/pytestlearning/Inputfiles/Addnewdata.json','r')
    request_json = json.loads(f.read())
    response=requests.post(API_URL,request_json)
    print(response.text)
    id1=jsonpath.jsonpath(response.json(),"id")
    print(id1)
    print(id1[0])
    tech_api_url="https://thetestingworldapi.com/api/technicalskills"
    f1=open("C:/Users/akhila.polasu/LERANpythonbasics/pytestlearning/Inputfiles/Addnewtechdata.json","r")
    request_json1=json.loads(f1.read())
    request_json1['id']=int(id1[0])
    request_json1['st_id'] = id1[0]
    response1=requests.post(tech_api_url,request_json1)
    #print(response1.text)
    Address_api_url = "https://thetestingworldapi.com/api/addresses"
    f2 = open("C:/Users/akhila.polasu/LERANpythonbasics/pytestlearning/Inputfiles/Addnewaddressdata.json", "r")
    request_json2 = json.loads(f2.read())
    request_json2['stId'] = id1[0]
    response2 = requests.post(Address_api_url,request_json2)
    #print(response2.text)
    final_details_url="https://thetestingworldapi.com/api/FinalStudentDetails/"+str(id1[0])
    response3=requests.get(final_details_url)
    print(response3.text)

