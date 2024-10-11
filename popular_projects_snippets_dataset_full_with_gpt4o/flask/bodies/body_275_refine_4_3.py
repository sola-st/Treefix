err = Exception('An error occurred') # pragma: no cover

class MockBaseException(Exception): pass # pragma: no cover
err = MockBaseException('This is a mock error message') # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/cli.py
from l3.Runtime import _l_
raise err from None
_l_(16935)
