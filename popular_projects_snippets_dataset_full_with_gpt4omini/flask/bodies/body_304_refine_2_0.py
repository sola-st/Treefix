from threading import RLock # pragma: no cover

self = type('Mock', (object,), {'lock': RLock()})() # pragma: no cover
obj = 'some_object_to_delete' # pragma: no cover

class MyBaseClass: pass # pragma: no cover

class MyBaseClass: pass # pragma: no cover
obj = 'some_object_to_delete' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/helpers.py
from l3.Runtime import _l_
with self.lock:
    _l_(7069)

    super().__delete__(obj)
    _l_(7068)
