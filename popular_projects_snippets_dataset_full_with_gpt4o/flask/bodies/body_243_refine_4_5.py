from typing import Any, Dict # pragma: no cover

value = {'example_tag': 'example_value'} # pragma: no cover
self = type('Mock', (object,), {'tags': {'example_tag': type('Tag', (object,), {'to_python': lambda self, x: x})()}})() # pragma: no cover

value = {'tag1': 'error_value'} # pragma: no cover
self = type('Mock', (object,), {'tags': {'tag1': type('Tag', (object,), {'to_python': lambda self, x: 'processed_' + x})()}})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/json/tag.py
from l3.Runtime import _l_
"""Convert a tagged representation back to the original type."""
if len(value) != 1:
    _l_(19674)

    aux = value
    _l_(19673)
    exit(aux)

key = next(iter(value))
_l_(19675)

if key not in self.tags:
    _l_(19677)

    aux = value
    _l_(19676)
    exit(aux)
aux = self.tags[key].to_python(value[key])
_l_(19678)

exit(aux)
