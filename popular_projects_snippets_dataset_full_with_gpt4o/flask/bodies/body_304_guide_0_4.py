import threading # pragma: no cover

class MockSuperClass: # pragma: no cover
    def __delete__(self, obj): # pragma: no cover
        print(f'Deleting {obj}') # pragma: no cover
 # pragma: no cover
class MockClass(MockSuperClass): # pragma: no cover
    def __init__(self): # pragma: no cover
        self.lock = threading.Lock() # pragma: no cover
 # pragma: no cover
self = MockClass() # pragma: no cover
obj = 'object to delete' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/helpers.py
from l3.Runtime import _l_
with self.lock:
    _l_(22765)

    super().__delete__(obj)
    _l_(22764)
