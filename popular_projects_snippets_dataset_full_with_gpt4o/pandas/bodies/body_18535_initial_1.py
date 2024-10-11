from datetime import datetime # pragma: no cover

MockStrptime = type('MockStrptime', (object,), {'_test_format_is_iso': lambda fmt: True if fmt == 'ISO_FORMAT_EXPECTED' else False}) # pragma: no cover
strptime = MockStrptime() # pragma: no cover
fmt = 'ISO_FORMAT_EXPECTED' # pragma: no cover
expected = True # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/tslibs/test_parsing.py
# see gh-41047
from l3.Runtime import _l_
result = strptime._test_format_is_iso(fmt)
_l_(19147)
assert result == expected
_l_(19148)
