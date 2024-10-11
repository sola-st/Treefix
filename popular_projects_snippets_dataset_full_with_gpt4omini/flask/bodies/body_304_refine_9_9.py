from threading import Lock # pragma: no cover

self = type('Mock', (object,), {'lock': Lock()})() # pragma: no cover
obj = 'sample_object' # pragma: no cover

from threading import Lock # pragma: no cover

class Example(object): # pragma: no cover
    def __delete__(self, obj): # pragma: no cover
        print(f'Deleting {obj}') # pragma: no cover
self = Example() # pragma: no cover
self.lock = Lock() # pragma: no cover
obj = 'test_object' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/helpers.py
from l3.Runtime import _l_
with self.lock:
    _l_(7069)

    super().__delete__(obj)
    _l_(7068)
