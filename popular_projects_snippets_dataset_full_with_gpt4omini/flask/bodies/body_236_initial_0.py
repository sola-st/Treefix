import uuid # pragma: no cover

UUID = uuid.UUID # pragma: no cover
value = '123e4567-e89b-12d3-a456-426614174000' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/json/tag.py
from l3.Runtime import _l_
aux = UUID(value)
_l_(3881)
exit(aux)
