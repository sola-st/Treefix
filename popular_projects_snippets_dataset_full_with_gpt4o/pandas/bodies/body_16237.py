# Extracted from ./data/repos/pandas/pandas/tests/series/test_logical_ops.py
s = Series([2, 3, 4, 5, 6, 7, 8, 9, datetime(2005, 1, 1)])
s[::2] = np.nan
d = DataFrame({"A": s})

expected = DataFrame(False, index=range(9), columns=["A"] + list(range(9)))

result = s & d
tm.assert_frame_equal(result, expected)

result = d & s
tm.assert_frame_equal(result, expected)
