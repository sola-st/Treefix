# Extracted from ./data/repos/pandas/pandas/tests/series/test_logical_ops.py
s = Series([2, 3, 4, 5, 6, 7, 8, 9, 10])

msg = "Cannot perform.+with a dtyped.+array and scalar of type"
with pytest.raises(TypeError, match=msg):
    s & datetime(2005, 1, 1)

s = Series([2, 3, 4, 5, 6, 7, 8, 9, datetime(2005, 1, 1)])
s[::2] = np.nan

expected = Series(True, index=s.index)
expected[::2] = False
result = s & list(s)
tm.assert_series_equal(result, expected)
