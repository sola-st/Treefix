# Extracted from ./data/repos/pandas/pandas/tests/window/test_rolling_functions.py
win = 25
ser = series[::2].resample("B").mean()
series_result = getattr(ser.rolling(window=win, min_periods=minp), roll_func)(
    **kwargs
)
last_date = series_result.index[-1]
prev_date = last_date - 24 * offsets.BDay()

trunc_series = series[::2].truncate(prev_date, last_date)
tm.assert_almost_equal(series_result[-1], compare_func(trunc_series))
