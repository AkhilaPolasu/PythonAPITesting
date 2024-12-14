import requests
import json
import jsonpath
def test_add_multiple_student():
    API_URL="https://thetestingworldapi.com/api/studentsDetails"
    f=open("C:/Users/akhila.polasu/LERANpythonbasics/pytestlearning/Inputfiles/Addnewmultiplstudent.json","r")
    input1=json.loads(f.read())
    request1=requests.post(API_URL,input1)
    print(request1.status_code)
    assert request1.status_code == 201