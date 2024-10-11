err = Exception('An error occurred') # pragma: no cover

class CustomError(Exception):# pragma: no cover
    pass# pragma: no cover
 # pragma: no cover
err = CustomError('An error occurred in CustomError') # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/cli.py
from l3.Runtime import _l_
raise err from None
_l_(16935)
