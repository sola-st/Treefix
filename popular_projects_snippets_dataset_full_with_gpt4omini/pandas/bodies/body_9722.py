# Extracted from ./data/repos/pandas/pandas/tests/window/test_timeseries_window.py

# compare for min_periods
df = regular

# these slightly different
expected = df.rolling(2, min_periods=1).sum()
result = df.rolling("2s").sum()
tm.assert_frame_equal(result, expected)

expected = df.rolling(2, min_periods=1).sum()
result = df.rolling("2s", min_periods=1).sum()
tm.assert_frame_equal(result, expected)
