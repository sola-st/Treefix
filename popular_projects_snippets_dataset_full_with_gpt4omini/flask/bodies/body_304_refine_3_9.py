from threading import Lock # pragma: no cover

self = type('Mock', (object,), {'lock': Lock()})() # pragma: no cover
obj = 'example_object' # pragma: no cover

from threading import Lock # pragma: no cover

class Mock:  # A mock class to provide the proper context for super(). # pragma: no cover
    def __delete__(self, obj): pass # pragma: no cover
self = Mock() # pragma: no cover
obj = 'item_to_delete' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/helpers.py
from l3.Runtime import _l_
with self.lock:
    _l_(7069)

    super().__delete__(obj)
    _l_(7068)
