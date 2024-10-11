from threading import RLock # pragma: no cover

self = type('Mock', (object,), {'lock': RLock()})() # pragma: no cover
obj = 'some_object_to_delete' # pragma: no cover

from threading import Lock # pragma: no cover

class Base: pass # pragma: no cover
self = type('Mock', (Base,), {'lock': Lock(), '__delete__': lambda self, obj: print(f'Deleting {obj}')})() # pragma: no cover
obj = 'object_to_delete' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/helpers.py
from l3.Runtime import _l_
with self.lock:
    _l_(7069)

    super().__delete__(obj)
    _l_(7068)
