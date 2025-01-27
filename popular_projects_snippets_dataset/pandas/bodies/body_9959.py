# Extracted from ./data/repos/pandas/pandas/tests/window/test_expanding.py
# GH 7512
df1 = DataFrame(
    [[1, 2], [3, 2], [3, 4]], columns=["A", "B"], index=Index(range(3), name="bar")
)
df1a = DataFrame(
    [[1, 2], [3, 4]], index=Index([0, 2], name="bar"), columns=["A", "B"]
)
df2 = DataFrame(
    [[5, 6], [None, None], [2, 1]],
    columns=["X", "Y"],
    index=Index(range(3), name="bar"),
)
df2a = DataFrame(
    [[5, 6], [2, 1]], index=Index([0, 2], name="bar"), columns=["X", "Y"]
)
result1 = df1.expanding().corr(df2, pairwise=True).loc[2]
result2 = df1.expanding().corr(df2a, pairwise=True).loc[2]
result3 = df1a.expanding().corr(df2, pairwise=True).loc[2]
result4 = df1a.expanding().corr(df2a, pairwise=True).loc[2]
expected = DataFrame(
    [[-1.0, -1.0], [-1.0, -1.0]], columns=["A", "B"], index=Index(["X", "Y"])
)
tm.assert_frame_equal(result1, expected)
tm.assert_frame_equal(result2, expected)
tm.assert_frame_equal(result3, expected)
tm.assert_frame_equal(result4, expected)
