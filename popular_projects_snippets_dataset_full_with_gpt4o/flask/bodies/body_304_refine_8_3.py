import threading # pragma: no cover

class MockSuper:# pragma: no cover
    def __delete__(self, obj):# pragma: no cover
        pass # pragma: no cover
class MockObject:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.lock = threading.Lock()# pragma: no cover
    def __delete__(self, obj):# pragma: no cover
        super().__delete__(obj) # pragma: no cover
self = MockObject() # pragma: no cover
obj = object() # pragma: no cover

import threading # pragma: no cover

class Base:# pragma: no cover
    def __delete__(self, obj):# pragma: no cover
        pass # pragma: no cover
class Mock(Base):# pragma: no cover
    def __init__(self):# pragma: no cover
        self.lock = threading.Lock() # pragma: no cover
self = Mock() # pragma: no cover
obj = object() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/helpers.py
from l3.Runtime import _l_
with self.lock:
    _l_(22765)

    super().__delete__(obj)
    _l_(22764)
