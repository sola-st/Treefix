import types # pragma: no cover

self = type('Mock', (), {'serializer': type('MockSerializer', (), {'tags': ['tag1', 'tag2']})()})() # pragma: no cover
value = {'tag1': 'value1'} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/json/tag.py
from l3.Runtime import _l_
aux = (
    isinstance(value, dict)
    and len(value) == 1
    and next(iter(value)) in self.serializer.tags
)
_l_(9661)
exit(aux)
