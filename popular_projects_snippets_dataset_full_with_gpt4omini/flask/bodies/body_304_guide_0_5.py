from threading import Lock # pragma: no cover
from unittest.mock import Mock # pragma: no cover

self = type('MockObject', (object,), {'lock': Lock(), '__delete__': Mock()})() # pragma: no cover
obj = 'some_object' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/helpers.py
from l3.Runtime import _l_
with self.lock:
    _l_(7069)

    super().__delete__(obj)
    _l_(7068)
