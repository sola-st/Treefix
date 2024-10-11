from threading import Lock # pragma: no cover

class Base: pass # pragma: no cover
class MockSuper(Base): # pragma: no cover
    def __delete__(self, obj): print(f'Deleting: {obj}') # pragma: no cover
self = type('Mock', (object,), {'lock': Lock(), '__delete__': MockSuper().__delete__})() # pragma: no cover
obj = 'item_to_delete' # pragma: no cover
super = MockSuper() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/helpers.py
from l3.Runtime import _l_
with self.lock:
    _l_(7069)

    super().__delete__(obj)
    _l_(7068)
