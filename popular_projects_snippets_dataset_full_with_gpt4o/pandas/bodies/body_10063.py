# Extracted from ./data/repos/pandas/pandas/tests/window/test_rolling_functions.py
win = 25
frm = frame[::2].resample("B").mean()
frame_result = getattr(frm.rolling(window=win, min_periods=minp), roll_func)(
    **kwargs
)
last_date = frame_result.index[-1]
prev_date = last_date - 24 * offsets.BDay()

trunc_frame = frame[::2].truncate(prev_date, last_date)
tm.assert_series_equal(
    frame_result.xs(last_date),
    trunc_frame.apply(compare_func, raw=raw),
    check_names=False,
)
