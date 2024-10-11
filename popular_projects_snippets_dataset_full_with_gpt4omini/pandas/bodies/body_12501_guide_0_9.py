import re # pragma: no cover

x = 'Some text' # pragma: no cover
def _remove_whitespace(string): return re.sub(r'\s+', '', string) # pragma: no cover
class Mock: pass # pragma: no cover
setattr(Mock, '_remove_whitespace', _remove_whitespace) # pragma: no cover
aux = Mock() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/io/test_html.py
from l3.Runtime import _l_
try:
    _l_(10240)

    aux = _remove_whitespace(x)
    _l_(10237)
    exit(aux)
except AttributeError:
    _l_(10239)

    aux = x
    _l_(10238)
    exit(aux)
