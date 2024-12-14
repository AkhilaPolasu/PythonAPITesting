import requests
import json
import jsonpath

def test_add_student_data():
    API_URL="https://thetestingworldapi.com/api/studentsDetails"
    file1=open("C:/Users/akhila.polasu/LERANpythonbasics/pytestlearning/Inputfiles/Requestjson.json","r")
    json_request=json.loads(file1.read())
    response=requests.post(API_URL,json_request)
    print(response.text)

def test_get_student_data():
    API_URL ="https://thetestingworldapi.com/api/studentsDetails/10508282"
    #id changes accordingly check id from the post url response
    response=requests.get(API_URL)
    print(response.text)
    print(response.status_code)
    #can write typecasting to json ->json_response=response.json()
    json_response=json.loads(response.text)
    id=jsonpath.jsonpath(json_response,"data.id")
    print(id)
    #assert id[0] == 10508282

def test_update_student_data():
    API_URL="https://thetestingworldapi.com/api/studentsDetails/10508282"
    file1=open("C:/Users/akhila.polasu/LERANpythonbasics/pytestlearning/Inputfiles/Updaterequest.json","r")
    json_request=json.loads(file1.read())
    response=requests.put(API_URL,json_request)
    print(response.text)

def test_delete_student_data():
    API_URL="https://thetestingworldapi.com/api/studentsDetails/10508282"
    response=requests.delete(API_URL)
    print(response.text)

def test_get1_student_data():
    API_URL ="https://thetestingworldapi.com/api/studentsDetails/10508282"
    #id changes accordingly check id from the post url response
    response=requests.get(API_URL)
    print(response.text)
    print(response.status_code)
    #can write typecasting to json ->json_response=response.json()
    json_response=json.loads(response.text)
    id=jsonpath.jsonpath(json_response,"data.id")
    print(id)


