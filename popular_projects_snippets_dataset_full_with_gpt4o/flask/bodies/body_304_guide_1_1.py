import threading # pragma: no cover

class Mock: # pragma: no cover
    lock = threading.Lock() # pragma: no cover
    def __delete__(self, obj): # pragma: no cover
        print(f'Deleted {obj}') # pragma: no cover
 # pragma: no cover
class Child(Mock): # pragma: no cover
    def __init__(self): # pragma: no cover
        self.lock = Mock.lock # pragma: no cover
 # pragma: no cover
self = Child() # pragma: no cover
obj = 'test_object' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/helpers.py
from l3.Runtime import _l_
with self.lock:
    _l_(22765)

    super().__delete__(obj)
    _l_(22764)
