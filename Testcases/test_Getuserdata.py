#API URL
import requests
import pytest
@pytest.mark.Smoke
def test_getuser():
    url="https://reqres.in/api/users?page=2"
    response=requests.get(url)
    print(response)
    #display response content
    print(response.content)
    print(response.headers)
    #response status code
    print(response.status_code)
    assert response.status_code == 200
    print(response.headers.get("Date"))
    print(response.headers.get("Server"))
    print(response.cookies)
    #fetch Encoding
    print(response.encoding)
    #elapsed time-time taken to request sent and response received
    print(response.elapsed)
