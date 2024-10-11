from threading import Lock # pragma: no cover

class Base: pass # pragma: no cover
class Derived(Base): # pragma: no cover
    def __delete__(self, obj): print(f'Deleted: {obj}') # pragma: no cover
self = type('Mock', (object,), {'lock': Lock(), '__delete__': Derived().__delete__})() # pragma: no cover
obj = 'test_object' # pragma: no cover
super = Derived() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/helpers.py
from l3.Runtime import _l_
with self.lock:
    _l_(7069)

    super().__delete__(obj)
    _l_(7068)
