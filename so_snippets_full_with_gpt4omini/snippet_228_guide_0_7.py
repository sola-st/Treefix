# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/159720/what-is-the-naming-convention-in-python-for-variable-and-function
from l3.Runtime import _l_
name = "John"
_l_(3041)

def display(name):
    _l_(3043)

    print("John")
    _l_(3042)

first_name = "John"
_l_(3044)

def display_first_name(first_name):
    _l_(3046)

    print(first_name)
    _l_(3045)

FIRST_NAME = "John"
_l_(3047)

