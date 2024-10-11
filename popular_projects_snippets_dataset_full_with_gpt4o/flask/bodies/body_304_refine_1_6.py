from threading import Lock # pragma: no cover

obj = object() # pragma: no cover
self = type('Mock', (object,), {'lock': Lock(), '__delete__': lambda self, obj: None})() # pragma: no cover

from threading import Lock # pragma: no cover

class Parent:# pragma: no cover
    def __delete__(self, obj):# pragma: no cover
        pass # pragma: no cover
class MockSelf(Parent):# pragma: no cover
    def __init__(self):# pragma: no cover
        self.lock = Lock() # pragma: no cover
self = MockSelf() # pragma: no cover
obj = object() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/helpers.py
from l3.Runtime import _l_
with self.lock:
    _l_(22765)

    super().__delete__(obj)
    _l_(22764)
