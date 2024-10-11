import sys # pragma: no cover
def _remove_whitespace(x): return x.strip() # pragma: no cover

x = '   Example string   ' # pragma: no cover
sys.exit = lambda aux: print('Exiting with:', aux) # pragma: no cover

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
