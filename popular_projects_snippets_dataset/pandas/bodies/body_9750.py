# Extracted from ./data/repos/pandas/pandas/tests/window/test_rolling_skew_kurt.py
import scipy.stats

compare_func = partial(getattr(scipy.stats, sp_func), bias=False)
result = getattr(series.rolling(50), roll_func)()
assert isinstance(result, Series)
tm.assert_almost_equal(result.iloc[-1], compare_func(series[-50:]))
