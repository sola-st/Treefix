from typing import Any # pragma: no cover

value = {'key': 'val'} # pragma: no cover
self = type('Mock', (object,), {'serializer': type('Mock', (object,), {'tags': {'key'}})()})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/json/tag.py
from l3.Runtime import _l_
aux = (
    isinstance(value, dict)
    and len(value) == 1
    and next(iter(value)) in self.serializer.tags
)
_l_(20896)
exit(aux)
