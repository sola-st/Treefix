err = Exception('An error occurred') # pragma: no cover

err = Exception('An error occurred')# pragma: no cover
try:# pragma: no cover
    raise err# pragma: no cover
except Exception as original_err:# pragma: no cover
    err.__cause__ = original_err # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/cli.py
from l3.Runtime import _l_
raise err from None
_l_(16935)
