import pytest
#Testcase must be written inside a method
#method must start with "test" else it is not recognised as the testcase
@pytest.mark.Smoke
def test_tc_002_Registration_testing():
    print("This is my Smoke testcase code")
    print("the testcase2 ended")

#print statement output to display on console -s
#verbose mode -v display the testcases name with pass or fail on the console
#pytest -v -s filename