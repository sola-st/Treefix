from typing import Any # pragma: no cover

self = type('Mock', (object,), {'serializer': None})() # pragma: no cover
serializer = {'serialize': lambda x: f'Serialized: {x}'} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/json/tag.py
from l3.Runtime import _l_
"""Create a tagger for the given serializer."""
self.serializer = serializer
_l_(6204)
