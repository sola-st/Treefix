import re # pragma: no cover

_remove_whitespace = lambda s: re.sub(r'\s+', ' ', s).strip() # pragma: no cover
x = '   Hello   World!   ' # pragma: no cover

import re # pragma: no cover

_remove_whitespace = lambda s: re.sub(r'\s+', ' ', s).strip() # pragma: no cover
x = '   Hello    World!   ' # pragma: no cover

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
