class MockBase: # pragma: no cover
    pass # pragma: no cover
class Mock(MockBase): # pragma: no cover
    pass # pragma: no cover
err = Mock() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/cli.py
from l3.Runtime import _l_
raise err from None
_l_(16935)
