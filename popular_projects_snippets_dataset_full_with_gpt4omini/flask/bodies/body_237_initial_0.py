from datetime import datetime # pragma: no cover

value = datetime.now() # pragma: no cover
datetime = datetime # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/json/tag.py
from l3.Runtime import _l_
aux = isinstance(value, datetime)
_l_(8900)
exit(aux)
