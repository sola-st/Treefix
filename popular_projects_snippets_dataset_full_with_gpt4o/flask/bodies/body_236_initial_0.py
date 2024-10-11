import uuid # pragma: no cover

UUID = uuid.UUID # pragma: no cover
value = '12345678123456781234567812345678' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/json/tag.py
from l3.Runtime import _l_
aux = UUID(value)
_l_(22467)
exit(aux)
