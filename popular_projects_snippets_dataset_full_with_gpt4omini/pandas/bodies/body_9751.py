# Extracted from ./data/repos/pandas/pandas/tests/window/test_rolling_skew_kurt.py
import scipy.stats

compare_func = partial(getattr(scipy.stats, sp_func), bias=False)
result = getattr(frame.rolling(50), roll_func)()
assert isinstance(result, DataFrame)
tm.assert_series_equal(
    result.iloc[-1, :],
    frame.iloc[-50:, :].apply(compare_func, axis=0, raw=raw),
    check_names=False,
)
