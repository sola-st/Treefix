# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_rank.py
obj = frame_or_series([np.inf, np.nan, -np.inf])
result = obj.rank(method=method, na_option=na_option, ascending=ascending)
expected = frame_or_series(expected)
tm.assert_equal(result, expected)
