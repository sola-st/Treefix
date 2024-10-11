import threading # pragma: no cover

class MockSuper:# pragma: no cover
    def __delete__(self, obj):# pragma: no cover
        print('MockSuper.__delete__ called')# pragma: no cover
 # pragma: no cover
self = type('Mock', (object,), {# pragma: no cover
    'lock': threading.Lock(),# pragma: no cover
    '__delete__': MockSuper.__delete__# pragma: no cover
})() # pragma: no cover
obj = 'test_object' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/helpers.py
from l3.Runtime import _l_
with self.lock:
    _l_(22765)

    super().__delete__(obj)
    _l_(22764)
