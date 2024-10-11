err = Exception('An error occurred') # pragma: no cover

err = None # pragma: no cover
try:# pragma: no cover
    raise Exception("An initial error")# pragma: no cover
except Exception as e:# pragma: no cover
    err = e # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/cli.py
from l3.Runtime import _l_
raise err from None
_l_(16935)
