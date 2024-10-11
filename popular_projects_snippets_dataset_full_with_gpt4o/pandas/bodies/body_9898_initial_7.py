from functools import partial # pragma: no cover
import pandas as pd # pragma: no cover
import numpy as np # pragma: no cover
pd.offsets.BDay # pragma: no cover
pd.testing.assert_series_equal # pragma: no cover

q = 0.5 # pragma: no cover
series = pd.Series(np.random.randn(100), index=pd.date_range('20230101', periods=100)) # pragma: no cover
offsets = type('Mock', (object,), {'BDay': pd.offsets.BDay}) # pragma: no cover
tm = type('Mock', (object,), {'assert_almost_equal': pd.testing.assert_series_equal}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/window/test_rolling_quantile.py
from l3.Runtime import _l_
compare_func = partial(scoreatpercentile, per=q)
_l_(18091)
win = 25
_l_(18092)
ser = series[::2].resample("B").mean()
_l_(18093)
series_result = ser.rolling(window=win, min_periods=10).quantile(q)
_l_(18094)
last_date = series_result.index[-1]
_l_(18095)
prev_date = last_date - 24 * offsets.BDay()
_l_(18096)

trunc_series = series[::2].truncate(prev_date, last_date)
_l_(18097)
tm.assert_almost_equal(series_result[-1], compare_func(trunc_series))
_l_(18098)
