# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_iloc.py
# GH#37728
df = DataFrame({"x": [1, 2], "y": [2, 2]})
rhs = {"x": 9, "y": 99}
df.iloc[1] = rhs
expected = DataFrame({"x": [1, 9], "y": [2, 99]})
tm.assert_frame_equal(df, expected)

# GH#38335 same thing, mixed dtypes
df = DataFrame({"x": [1, 2], "y": [2.0, 2.0]})
df.iloc[1] = rhs
expected = DataFrame({"x": [1, 9], "y": [2.0, 99.0]})
tm.assert_frame_equal(df, expected)
