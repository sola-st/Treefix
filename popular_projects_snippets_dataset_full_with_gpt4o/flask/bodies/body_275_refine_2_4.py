err = Exception('This is a sample error message') # pragma: no cover

try:# pragma: no cover
    raise Exception('Initial error')# pragma: no cover
except Exception as cause:# pragma: no cover
    err = Exception('Chained error occurred')# pragma: no cover
    err.__cause__ = cause # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/cli.py
from l3.Runtime import _l_
raise err from None
_l_(16935)
