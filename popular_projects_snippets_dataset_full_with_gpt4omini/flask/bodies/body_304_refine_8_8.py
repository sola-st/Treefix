from threading import Lock # pragma: no cover
from typing import Any # pragma: no cover

self = type('Mock', (object,), {'lock': Lock()})() # pragma: no cover
obj = 'sample_object' # pragma: no cover

from threading import Lock # pragma: no cover

class Container: pass # pragma: no cover
self = Container() # pragma: no cover
self.lock = Lock() # pragma: no cover
obj = 'example_object' # pragma: no cover
setattr(self, '__delete__', lambda obj: None) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/helpers.py
from l3.Runtime import _l_
with self.lock:
    _l_(7069)

    super().__delete__(obj)
    _l_(7068)
