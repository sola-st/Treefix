import threading # pragma: no cover

class BaseClass: # pragma: no cover
    def __delete__(self, obj): # pragma: no cover
        print(f'Deleting {obj}') # pragma: no cover
 # pragma: no cover
self = type('Mock', (BaseClass,), {'lock': threading.Lock()})() # pragma: no cover
obj = 'test_object' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/helpers.py
from l3.Runtime import _l_
with self.lock:
    _l_(22765)

    super().__delete__(obj)
    _l_(22764)
