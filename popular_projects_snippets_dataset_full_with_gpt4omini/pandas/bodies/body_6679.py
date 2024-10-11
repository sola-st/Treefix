# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_frozen.py
def setitem():
    container[0] = 5

self.check_mutable_error(setitem)

def setslice():
    container[1:2] = 3

self.check_mutable_error(setslice)

def delitem():
    del container[0]

self.check_mutable_error(delitem)

def delslice():
    del container[0:3]

self.check_mutable_error(delslice)

mutable_methods = ("extend", "pop", "remove", "insert")

for meth in mutable_methods:
    self.check_mutable_error(getattr(container, meth))
