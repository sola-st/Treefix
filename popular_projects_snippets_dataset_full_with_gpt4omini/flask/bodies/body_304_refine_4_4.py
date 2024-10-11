from threading import RLock # pragma: no cover

self = type('Mock', (object,), {'lock': RLock()})() # pragma: no cover
obj = 'example_object' # pragma: no cover

from threading import RLock # pragma: no cover

class Mock: # pragma: no cover
    def __delete__(self, obj): # pragma: no cover
        print(f'Deleting {obj}') # pragma: no cover
self = Mock() # pragma: no cover
obj = 'example_object' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/helpers.py
from l3.Runtime import _l_
with self.lock:
    _l_(7069)

    super().__delete__(obj)
    _l_(7068)
