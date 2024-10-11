from functools import partial # pragma: no cover
from scipy.stats import scoreatpercentile # pragma: no cover
import pandas as pd # pragma: no cover
from pandas import offsets # pragma: no cover
import numpy as np # pragma: no cover
import pandas.testing as tm # pragma: no cover

q = 0.5 # pragma: no cover
series = pd.Series(np.random.randn(100), index=pd.date_range('2023-01-01', periods=100, freq='D')) # pragma: no cover
offsets = type('Mock', (object,), {'BDay': lambda: pd.offsets.BDay()})() # pragma: no cover
tm = type('Mock', (object,), {'assert_almost_equal': lambda a, b: print('Assertion passed' if np.isclose(a, b) else 'Assertion failed')})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/window/test_rolling_quantile.py
from l3.Runtime import _l_
compare_func = partial(scoreatpercentile, per=q)
_l_(6171)
win = 25
_l_(6172)
ser = series[::2].resample("B").mean()
_l_(6173)
series_result = ser.rolling(window=win, min_periods=10).quantile(q)
_l_(6174)
last_date = series_result.index[-1]
_l_(6175)
prev_date = last_date - 24 * offsets.BDay()
_l_(6176)

trunc_series = series[::2].truncate(prev_date, last_date)
_l_(6177)
tm.assert_almost_equal(series_result[-1], compare_func(trunc_series))
_l_(6178)
