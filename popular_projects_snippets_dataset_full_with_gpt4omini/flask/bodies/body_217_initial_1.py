import json # pragma: no cover

self = type('Mock', (object,), {'key': 'example_key', 'to_json': lambda self, value: json.dumps(value)})() # pragma: no cover
value = {'example': 'data'} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/json/tag.py
from l3.Runtime import _l_
"""Convert the value to a valid JSON type and add the tag structure
        around it."""
aux = {self.key: self.to_json(value)}
_l_(7066)
exit(aux)
