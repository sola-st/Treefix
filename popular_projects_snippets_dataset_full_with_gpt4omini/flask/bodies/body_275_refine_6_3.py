Exception # pragma: no cover

err = Exception('An error occurred') # pragma: no cover

err = RuntimeError('An example of a runtime error') # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/cli.py
from l3.Runtime import _l_
raise err from None
_l_(5203)
