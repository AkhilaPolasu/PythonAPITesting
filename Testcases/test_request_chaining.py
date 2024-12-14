import json
import jsonpath
import requests
def test_Add_new_student():
    global id
    API_URL="https://thetestingworldapi.com/api/studentsDetails"
    f1=open("C:/Users/akhila.polasu/LERANpythonbasics/pytestlearning/Inputfiles/Addnewstreqchaining.json","r")
    input_json=json.loads(f1.read())
    response=requests.post(API_URL,input_json)
    print(response.text)
    id=jsonpath.jsonpath(response.json(),"id")
    print(id[0])

def test_get_details():
    API_URL="https://thetestingworldapi.com/api/studentsDetails/"+str(id[0])
    response=requests.get(API_URL)
    print(response.text)
