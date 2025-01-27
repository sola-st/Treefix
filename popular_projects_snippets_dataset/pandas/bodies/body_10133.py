# Extracted from ./data/repos/pandas/pandas/tests/window/test_apply.py
win = 25
minp = 10
ser = series[::2].resample("B").mean()
series_result = ser.rolling(window=win, min_periods=minp).apply(f, raw=raw)
last_date = series_result.index[-1]
prev_date = last_date - 24 * offsets.BDay()

trunc_series = series[::2].truncate(prev_date, last_date)
tm.assert_almost_equal(series_result[-1], np.mean(trunc_series))
