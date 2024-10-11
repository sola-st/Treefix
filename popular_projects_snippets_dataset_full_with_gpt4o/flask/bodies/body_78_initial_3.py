from datetime import timedelta # pragma: no cover

value = 5 # pragma: no cover
timedelta = timedelta # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/app.py
from l3.Runtime import _l_
if value is None or isinstance(value, timedelta):
    _l_(18347)

    aux = value
    _l_(18346)
    exit(aux)
aux = timedelta(seconds=value)
_l_(18348)

exit(aux)
