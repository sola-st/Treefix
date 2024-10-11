import pandas as pd # pragma: no cover
import pytest # pragma: no cover
import pandas.testing as tm # pragma: no cover

period_range = pd.period_range # pragma: no cover
PeriodIndex = pd.PeriodIndex # pragma: no cover
tm = type('Mock', (object,), {'assert_index_equal': tm.assert_index_equal})() # pragma: no cover
pytest = type('Mock', (object,), {'raises': pytest.raises})() # pragma: no cover

import pandas as pd # pragma: no cover
import pytest # pragma: no cover
import pandas.testing as tm # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/test_constructors.py
# GH #7811
from l3.Runtime import _l_
pidx = period_range(start="2014-01", freq="2M", periods=4)
_l_(6742)
expected = PeriodIndex(["2014-01", "2014-03", "2014-05", "2014-07"], freq="2M")
_l_(6743)
tm.assert_index_equal(pidx, expected)
_l_(6744)

pidx = period_range(start="2014-01-02", end="2014-01-15", freq="3D")
_l_(6745)
expected = PeriodIndex(
    ["2014-01-02", "2014-01-05", "2014-01-08", "2014-01-11", "2014-01-14"],
    freq="3D",
)
_l_(6746)
tm.assert_index_equal(pidx, expected)
_l_(6747)

pidx = period_range(end="2014-01-01 17:00", freq="4H", periods=3)
_l_(6748)
expected = PeriodIndex(
    ["2014-01-01 09:00", "2014-01-01 13:00", "2014-01-01 17:00"], freq="4H"
)
_l_(6749)
tm.assert_index_equal(pidx, expected)
_l_(6750)

msg = "Frequency must be positive, because it represents span: -1M"
_l_(6751)
with pytest.raises(ValueError, match=msg):
    _l_(6753)

    PeriodIndex(["2011-01"], freq="-1M")
    _l_(6752)

msg = "Frequency must be positive, because it represents span: 0M"
_l_(6754)
with pytest.raises(ValueError, match=msg):
    _l_(6756)

    PeriodIndex(["2011-01"], freq="0M")
    _l_(6755)

msg = "Frequency must be positive, because it represents span: 0M"
_l_(6757)
with pytest.raises(ValueError, match=msg):
    _l_(6759)

    period_range("2011-01", periods=3, freq="0M")
    _l_(6758)
