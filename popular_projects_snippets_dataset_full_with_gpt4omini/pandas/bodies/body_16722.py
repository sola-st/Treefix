# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge.py
# GH21119: bool + object bool merge OK
df1 = DataFrame({"key": Series([True, False], dtype=object)})
df2 = DataFrame({"key": [True, False]})

expected = DataFrame({"key": [True, False]}, dtype=object)
result = merge(df1, df2, on="key")
tm.assert_frame_equal(result, expected)
result = merge(df2, df1, on="key")
tm.assert_frame_equal(result, expected)
