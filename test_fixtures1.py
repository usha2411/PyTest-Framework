import pytest

@pytest.fixture()

def method1():                          #method which we want to execute before def
    print("Welcome to Pune")

def testMethod2(method1):                #write method in bracket which we want to execute before
    print("Hello,How are you")

def testMwthod3(method1 ):
    print("What is your name")