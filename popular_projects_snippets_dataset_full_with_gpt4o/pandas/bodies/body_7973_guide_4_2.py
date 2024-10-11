from pandas import period_range, PeriodIndex # pragma: no cover
import pytest # pragma: no cover

class MockTM: # pragma: no cover
    @staticmethod # pragma: no cover
    def assert_index_equal(left, right): # pragma: no cover
        assert left.equals(right), f'{left} != {right}' # pragma: no cover
 # pragma: no cover
tm = MockTM() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/test_constructors.py
# GH #7811
from l3.Runtime import _l_
pidx = period_range(start="2014-01", freq="2M", periods=4)
_l_(16961)
expected = PeriodIndex(["2014-01", "2014-03", "2014-05", "2014-07"], freq="2M")
_l_(16962)
tm.assert_index_equal(pidx, expected)
_l_(16963)

pidx = period_range(start="2014-01-02", end="2014-01-15", freq="3D")
_l_(16964)
expected = PeriodIndex(
    ["2014-01-02", "2014-01-05", "2014-01-08", "2014-01-11", "2014-01-14"],
    freq="3D",
)
_l_(16965)
tm.assert_index_equal(pidx, expected)
_l_(16966)

pidx = period_range(end="2014-01-01 17:00", freq="4H", periods=3)
_l_(16967)
expected = PeriodIndex(
    ["2014-01-01 09:00", "2014-01-01 13:00", "2014-01-01 17:00"], freq="4H"
)
_l_(16968)
tm.assert_index_equal(pidx, expected)
_l_(16969)

msg = "Frequency must be positive, because it represents span: -1M"
_l_(16970)
with pytest.raises(ValueError, match=msg):
    _l_(16972)

    PeriodIndex(["2011-01"], freq="-1M")
    _l_(16971)

msg = "Frequency must be positive, because it represents span: 0M"
_l_(16973)
with pytest.raises(ValueError, match=msg):
    _l_(16975)

    PeriodIndex(["2011-01"], freq="0M")
    _l_(16974)

msg = "Frequency must be positive, because it represents span: 0M"
_l_(16976)
with pytest.raises(ValueError, match=msg):
    _l_(16978)

    period_range("2011-01", periods=3, freq="0M")
    _l_(16977)
