# Extracted from ./data/repos/pandas/pandas/tests/window/test_rolling_quantile.py
compare_func = partial(scoreatpercentile, per=q)
win = 25
frm = frame[::2].resample("B").mean()
frame_result = frm.rolling(window=win, min_periods=10).quantile(q)
last_date = frame_result.index[-1]
prev_date = last_date - 24 * offsets.BDay()

trunc_frame = frame[::2].truncate(prev_date, last_date)
tm.assert_series_equal(
    frame_result.xs(last_date),
    trunc_frame.apply(compare_func, raw=raw),
    check_names=False,
)
