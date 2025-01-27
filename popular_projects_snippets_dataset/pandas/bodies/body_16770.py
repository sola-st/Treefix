# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge.py
# GH 13353
df1 = DataFrame([[1, 2], [3, 4]], columns=Index(["a", 114.0]))
df2 = DataFrame([[9, 10], [11, 12]], columns=["x", "y"])
result = merge(df2, df1, how="inner", left_index=True, right_index=True)
expected = DataFrame(
    [[9, 10, 1, 2], [11, 12, 3, 4]], columns=Index(["x", "y", "a", 114.0])
)
tm.assert_frame_equal(result, expected)
