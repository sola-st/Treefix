# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_iloc.py
# GH#20438 testing specifically list key, not arraylike
ser = Series([0, 1, 2])
ser.iloc[indexing_func([True, False, True])] = rhs_func([5, 10])
expected = Series([5, 1, 10])
tm.assert_series_equal(ser, expected)

df = DataFrame({"a": [0, 1, 2]})
df.iloc[indexing_func([True, False, True])] = rhs_func([[5], [10]])
expected = DataFrame({"a": [5, 1, 10]})
tm.assert_frame_equal(df, expected)
