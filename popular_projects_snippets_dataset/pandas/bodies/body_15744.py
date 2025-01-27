# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_pct_change.py
# GH#7292
rs_freq = datetime_series.pct_change(
    freq=freq, fill_method=fill_method, limit=limit
)
rs_periods = datetime_series.pct_change(
    periods, fill_method=fill_method, limit=limit
)
tm.assert_series_equal(rs_freq, rs_periods)

empty_ts = Series(index=datetime_series.index, dtype=object)
rs_freq = empty_ts.pct_change(freq=freq, fill_method=fill_method, limit=limit)
rs_periods = empty_ts.pct_change(periods, fill_method=fill_method, limit=limit)
tm.assert_series_equal(rs_freq, rs_periods)
