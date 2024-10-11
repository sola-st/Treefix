self = type('Mock', (dict,), {})({'a': 1, 'b': 2}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/config.py
from l3.Runtime import _l_
aux = f"<{type(self).__name__} {dict.__repr__(self)}>"
_l_(22629)
exit(aux)
