# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/methods/test_asfreq.py
from l3.Runtime import _l_
idx = PeriodIndex(["2011-01", "2011-02", "NaT", "2011-04"], freq="M")
_l_(20670)
result = idx.asfreq(freq="Q")
_l_(20671)
expected = PeriodIndex(["2011Q1", "2011Q1", "NaT", "2011Q2"], freq="Q")
_l_(20672)
tm.assert_index_equal(result, expected)
_l_(20673)
