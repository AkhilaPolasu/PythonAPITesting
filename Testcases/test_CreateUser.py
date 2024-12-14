import requests
import json
import jsonpath
import pytest
url="https://reqres.in/api/users"
a=11
#@pytest.mark.skip("this is not valid for current build")
#@pytest.mark.skipif(a>10,reason="this is not valid for current build")

@pytest.fixture(scope="module")
def start_exec():
    print("This is the fixture code")
    yield
    print("This the end of Fixture code")
@pytest.mark.Smoke
def test_new_User(start_exec):
    response=requests.get(url)
    #read input json file
    file1=open('C:/Users/akhila.polasu/LERANpythonbasics/pytestlearning/createuser.json', 'r')
    json_input=file1.read()
    print(type(json_input))
    j1=json.loads(json_input)
    print(type(j1))
    print(j1)
    #make a POST request with the json input body
    # in post we need to pass two arguments, 1 is url and other is input file
    r1=requests.post(url,j1)
    print(r1)
    print(r1.content)
    #validating response code
    assert r1.status_code == 201
    #fetch header from response
    print(r1.headers)
    print(r1.headers.get('Content-Length'))
    #parse response to json format
    res=json.loads(r1.text)
    #pick a json path
    result=jsonpath1=jsonpath.jsonpath(res,'id')
    print(result)
    print(result[0])
@pytest.mark.Sanity
def test_other_Create_User(start_exec):
    response=requests.get(url)
    #read input json file
    file1=open('C:/Users/akhila.polasu/LERANpythonbasics/pytestlearning/createuser.json', 'r')
    json_input=file1.read()
    print(type(json_input))
    j1=json.loads(json_input)
    print(type(j1))
    print(j1)
    #make a POST request with the json input body
    # in post we need to pass two arguments, 1 is url and other is input file
    r1=requests.post(url,j1)
    print(r1)
    print(r1.content)
    #validating response code
    assert r1.status_code == 201
    #fetch header from response
    print(r1.headers)
    print(r1.headers.get('Content-Length'))
    #parse response to json format
    res=json.loads(r1.text)
    #pick a json path
    result=jsonpath1=jsonpath.jsonpath(res,'id')
    print(result)
    print(result[0])