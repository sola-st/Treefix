from datetime import datetime # pragma: no cover

value = datetime(2023, 10, 1, 0, 0) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/json/tag.py
from l3.Runtime import _l_
aux = isinstance(value, datetime)
_l_(20077)
exit(aux)
