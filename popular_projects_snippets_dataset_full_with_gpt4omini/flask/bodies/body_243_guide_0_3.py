from typing import Any, Dict # pragma: no cover

value = { 'tag1': 'sample_value' } # pragma: no cover
self = type('Mock', (), {'tags': {'tag1': type('Mock', (), {'to_python': lambda self, val: val})()}})() # pragma: no cover

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
