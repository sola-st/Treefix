from typing import Optional # pragma: no cover

value = 'http://example.com/' # pragma: no cover
self = type('Mock', (object,), {'_static_url_path': ''})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/scaffold.py
from l3.Runtime import _l_
if value is not None:
    _l_(9312)

    value = value.rstrip("/")
    _l_(9311)

self._static_url_path = value
_l_(9313)
