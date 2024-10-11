# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_pct_change.py
# GH#7292
rs_freq = datetime_frame.pct_change(
    freq=freq, fill_method=fill_method, limit=limit
)
rs_periods = datetime_frame.pct_change(
    periods, fill_method=fill_method, limit=limit
)
tm.assert_frame_equal(rs_freq, rs_periods)

empty_ts = DataFrame(index=datetime_frame.index, columns=datetime_frame.columns)
rs_freq = empty_ts.pct_change(freq=freq, fill_method=fill_method, limit=limit)
rs_periods = empty_ts.pct_change(periods, fill_method=fill_method, limit=limit)
tm.assert_frame_equal(rs_freq, rs_periods)
