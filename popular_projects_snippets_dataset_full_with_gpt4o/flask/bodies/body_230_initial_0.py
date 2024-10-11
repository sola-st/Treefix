import base64 # pragma: no cover

b64decode = base64.b64decode # pragma: no cover
value = 'aGVsbG8gd29ybGQ=' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/json/tag.py
from l3.Runtime import _l_
aux = b64decode(value)
_l_(22489)
exit(aux)
