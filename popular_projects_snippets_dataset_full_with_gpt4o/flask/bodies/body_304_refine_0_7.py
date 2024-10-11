import threading # pragma: no cover

obj = type('MockObject', (object,), {})() # pragma: no cover
self = type('MockSelf', (object,), {'lock': threading.Lock()})() # pragma: no cover

import threading # pragma: no cover

class ParentClass:# pragma: no cover
    def __delete__(self, obj):# pragma: no cover
        pass # pragma: no cover
obj = type('MockObject', (object,), {})() # pragma: no cover
self = type('MockSelf', (ParentClass,), {'lock': threading.Lock()})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/helpers.py
from l3.Runtime import _l_
with self.lock:
    _l_(22765)

    super().__delete__(obj)
    _l_(22764)
