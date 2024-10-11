err = Exception('An error occurred') # pragma: no cover

class DummyBaseException(Exception): # pragma: no cover
    pass # pragma: no cover
err = DummyBaseException('An error occurred') # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/cli.py
from l3.Runtime import _l_
raise err from None
_l_(16935)
