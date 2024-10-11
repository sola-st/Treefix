# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py

# xref 8260
# uniform returns a DatetimeIndex
from l3.Runtime import _l_
arr = [
    Timestamp("2013-01-01 13:00:00-0800", tz="US/Pacific"),
    Timestamp("2013-01-02 14:00:00-0800", tz="US/Pacific"),
]
_l_(9387)
result = to_datetime(arr, cache=cache)
_l_(9388)
expected = DatetimeIndex(
    ["2013-01-01 13:00:00", "2013-01-02 14:00:00"], tz="US/Pacific"
)
_l_(9389)
tm.assert_index_equal(result, expected)
_l_(9390)
