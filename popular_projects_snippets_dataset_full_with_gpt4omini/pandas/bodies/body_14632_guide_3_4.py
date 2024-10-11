import pandas as pd # pragma: no cover
import pandas.testing as tm # pragma: no cover
from pandas import date_range # pragma: no cover
from pandas import DatetimeIndex # pragma: no cover

_ = None # pragma: no cover
x = date_range(start='2012-01-02', periods=10, freq='D') # pragma: no cover
y = list(range(len(x))) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_datetimelike.py
from l3.Runtime import _l_
x = date_range(start="2012-01-02", periods=10, freq="D")
_l_(9298)
y = list(range(len(x)))
_l_(9299)
_, ax = self.plt.subplots()
_l_(9300)
lines = ax.plot(x, y, label="Y")
_l_(9301)
tm.assert_index_equal(DatetimeIndex(lines[0].get_xdata()), x)
_l_(9302)
