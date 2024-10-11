from datetime import datetime # pragma: no cover

class MockStrptime: # pragma: no cover
    @staticmethod # pragma: no cover
    def _test_format_is_iso(fmt): # pragma: no cover
        return fmt == '%Y-%m-%dT%H:%M:%S' # pragma: no cover
strptime = MockStrptime() # pragma: no cover
fmt = '%Y-%m-%dT%H:%M:%S' # pragma: no cover
expected = True # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/tslibs/test_parsing.py
# see gh-41047
from l3.Runtime import _l_
result = strptime._test_format_is_iso(fmt)
_l_(8959)
assert result == expected
_l_(8960)
