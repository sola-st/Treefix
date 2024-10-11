import threading # pragma: no cover

self = type('Mock', (object,), {'lock': threading.Lock()})() # pragma: no cover
obj = 'some_object' # pragma: no cover

import threading # pragma: no cover

class Base:# pragma: no cover
    def __delete__(self, obj):# pragma: no cover
        print(f'Deleting {obj}') # pragma: no cover
class Mock(Base):# pragma: no cover
    lock = threading.Lock() # pragma: no cover
self = Mock() # pragma: no cover
obj = object() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/helpers.py
from l3.Runtime import _l_
with self.lock:
    _l_(22765)

    super().__delete__(obj)
    _l_(22764)
