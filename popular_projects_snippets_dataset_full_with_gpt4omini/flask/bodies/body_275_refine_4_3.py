Exception # pragma: no cover

err = Exception('This is a mock exception') # pragma: no cover

class MockException(Exception): pass # pragma: no cover
err = MockException('This is a mock exception') # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/cli.py
from l3.Runtime import _l_
raise err from None
_l_(5203)
