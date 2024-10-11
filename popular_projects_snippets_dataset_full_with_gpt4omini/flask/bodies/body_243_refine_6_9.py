from collections import defaultdict # pragma: no cover

value = {'key1': 'value1'} # pragma: no cover
self = type('Mock', (), {'tags': {'key1': type('MockTag', (), {'to_python': lambda self, v: v.upper()})()}})() # pragma: no cover

from typing import Dict, Any # pragma: no cover

value = {'key1': 'value1'} # pragma: no cover
self = type('Mock', (object,), {'tags': {'key1': type('MockTag', (object,), {'to_python': lambda self, v: v})()}})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/json/tag.py
from l3.Runtime import _l_
"""Convert a tagged representation back to the original type."""
if len(value) != 1:
    _l_(8594)

    aux = value
    _l_(8593)
    exit(aux)

key = next(iter(value))
_l_(8595)

if key not in self.tags:
    _l_(8597)

    aux = value
    _l_(8596)
    exit(aux)
aux = self.tags[key].to_python(value[key])
_l_(8598)

exit(aux)
