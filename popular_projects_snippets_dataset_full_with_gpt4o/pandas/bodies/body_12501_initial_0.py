def _remove_whitespace(s):# pragma: no cover
    return s.replace(' ', '') # pragma: no cover
x = 'example string with spaces' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/io/test_html.py
from l3.Runtime import _l_
try:
    _l_(21298)

    aux = _remove_whitespace(x)
    _l_(21295)
    exit(aux)
except AttributeError:
    _l_(21297)

    aux = x
    _l_(21296)
    exit(aux)
