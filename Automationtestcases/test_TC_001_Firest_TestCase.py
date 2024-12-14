import pytest
#Testcase must be written inside a method
#method must start with "test" else it is not recognised as the testcase
a=101
actual_result ="testing"
#for skipping the specific testcase ,use this decorator accordingly with if or without(conditionally)
#@pytest.mark.skipif(a>100,reason="skipping this testcase, as this functionally is not working, devloper will fix it")
@pytest.mark.TopPriority
def test_tc_001_login_logout_testing():
    print("This is my Smoke-testcase")
    print("the testcase1 ended")
    assert actual_result != "testing","These 2 values should not be same"

#second testcase in same file
@pytest.mark.TopPriority
def test_tc_003_login_logout_Invalid_Credentials():
    print("This is my Sanity testcase")
    print("the testcase3 ended")