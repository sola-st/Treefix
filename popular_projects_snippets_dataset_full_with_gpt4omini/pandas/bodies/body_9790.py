# Extracted from ./data/repos/pandas/pandas/tests/window/test_win_type.py
# GitHub Issue #46772
x = Series(0)
result = x.rolling(window=16, center=center, win_type=win_types).var()
expected = Series(np.NaN)

tm.assert_series_equal(result, expected)
