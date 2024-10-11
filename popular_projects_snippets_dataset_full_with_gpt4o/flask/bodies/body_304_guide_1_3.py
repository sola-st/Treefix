import threading # pragma: no cover

class SuperClass: # pragma: no cover
    def __delete__(self, obj): # pragma: no cover
        print(f"Deleted: {obj}") # pragma: no cover
 # pragma: no cover
class MockClass(SuperClass): # pragma: no cover
    def __init__(self): # pragma: no cover
        self.lock = threading.Lock() # pragma: no cover
 # pragma: no cover
mock_class = MockClass() # pragma: no cover
self = mock_class # pragma: no cover
obj = "TestObject" # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/helpers.py
from l3.Runtime import _l_
with self.lock:
    _l_(22765)

    super().__delete__(obj)
    _l_(22764)
