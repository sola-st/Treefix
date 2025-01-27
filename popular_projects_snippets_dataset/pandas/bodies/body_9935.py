# Extracted from ./data/repos/pandas/pandas/tests/window/test_expanding.py
# GH 25857
result = frame_or_series(range(5)).expanding(min_periods=6).count()
expected = frame_or_series([np.nan, np.nan, np.nan, np.nan, np.nan])
tm.assert_equal(result, expected)
