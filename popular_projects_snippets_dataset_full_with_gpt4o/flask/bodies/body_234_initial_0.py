from uuid import UUID # pragma: no cover
from uuid import uuid4 # pragma: no cover

value = uuid4() # pragma: no cover
UUID = UUID # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/json/tag.py
from l3.Runtime import _l_
aux = isinstance(value, UUID)
_l_(22622)
exit(aux)
