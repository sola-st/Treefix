from datetime import datetime # pragma: no cover

def parse_date(value):# pragma: no cover
    try:# pragma: no cover
        return datetime.strptime(value, '%Y-%m-%d')# pragma: no cover
    except ValueError:# pragma: no cover
        return None # pragma: no cover
value = '2023-10-10' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/json/tag.py
from l3.Runtime import _l_
aux = parse_date(value)
_l_(20153)
exit(aux)
