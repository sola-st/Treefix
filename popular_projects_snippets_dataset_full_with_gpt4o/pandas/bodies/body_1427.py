# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_indexing.py
index = Index([-5, 0, 5], name="z")
df = DataFrame({"x": [1, 2, 6], "y": [2, 2, 8]}, index=index)
expected = df.copy()
rhs = {"x": 9, "y": 99}
df.loc[5] = rhs
expected.loc[5] = [9, 99]
tm.assert_frame_equal(df, expected)

# GH#38335 same thing, mixed dtypes
df = DataFrame({"x": [1, 2, 6], "y": [2.0, 2.0, 8.0]}, index=index)
df.loc[5] = rhs
expected = DataFrame({"x": [1, 2, 9], "y": [2.0, 2.0, 99.0]}, index=index)
tm.assert_frame_equal(df, expected)
