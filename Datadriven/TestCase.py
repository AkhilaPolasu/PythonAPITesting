import json
import jsonpath
import requests
import openpyxl
from Datadriven import Library

def test_add_multiple_students():
    API_URL="http://thetestingworldapi.com/api/studentsDetails"
    f=open("C:/Users/akhila.polasu/LERANpythonbasics/pytestlearning/Inputfiles/Addnewmultiplstudent.json","r")
    json_request = json.loads(f.read())
    print(json_request)

    obj=Library.Commom("C:/Users/akhila.polasu/OneDrive - Calsoft Pvt Ltd/Desktop/EXELFiles/Book 6.xlsx","Sheet2")
    col=obj.fetch_column_count()
    row=obj.fetch_row_count()
    keyList1=obj.fetch_key_names()

    for i in range(2,row+1):
        updated_json_request=obj.update_request_with_data(i,json_request,keyList1)
        response=requests.post(API_URL,updated_json_request)
        print(response)