import pytest

def details():
    print("Enter Details")
    yield
    print("Welcome to Login")

def testLogin():
    print("Successfully Login")

@pytest.mark.sanity
def testLogout():
    print("Successfully Logout")