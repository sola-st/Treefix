import threading # pragma: no cover

self = type('Mock', (object,), {'lock': threading.Lock()})() # pragma: no cover
obj = 'some_object' # pragma: no cover

import threading # pragma: no cover

class BaseClass:# pragma: no cover
    def __delete__(self, obj):# pragma: no cover
        pass # pragma: no cover
class DerivedClass(BaseClass):# pragma: no cover
    lock = threading.Lock() # pragma: no cover
self = DerivedClass() # pragma: no cover
obj = object() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/helpers.py
from l3.Runtime import _l_
with self.lock:
    _l_(22765)

    super().__delete__(obj)
    _l_(22764)
