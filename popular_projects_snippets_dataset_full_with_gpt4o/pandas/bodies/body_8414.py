# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_date_range.py
# smoke test
from l3.Runtime import _l_
start = Timestamp("20130220 10:00", tz="US/Eastern")
_l_(21654)
result = date_range(start, periods=2, tz="US/Eastern")
_l_(21655)
assert len(result) == 2
_l_(21656)
