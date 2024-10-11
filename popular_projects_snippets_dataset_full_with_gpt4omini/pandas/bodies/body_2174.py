# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
# https://github.com/pandas-dev/pandas/issues/12649
from l3.Runtime import _l_
expected = Timestamp(2012, 1, 1)
_l_(7809)
result = to_datetime(input, format=format, exact=False)
_l_(7810)
assert result == expected
_l_(7811)
