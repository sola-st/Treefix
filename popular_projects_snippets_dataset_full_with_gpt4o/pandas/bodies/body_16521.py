# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_crosstab.py
# GH#12578
df = DataFrame(
    {"a": [1, 2, 2, 2, 2], "b": [3, 3, 4, 4, 4], "c": [1, 1, np.nan, 1, 1]}
)

# Test arrays
crosstab(
    [np.array([1, 1, 2, 2]), np.array([1, 2, 1, 2])], np.array([1, 2, 1, 2])
)

# Test with aggfunc
norm_counts = DataFrame(
    [[0.25, 0, 0.25], [0.25, 0.5, 0.75], [0.5, 0.5, 1]],
    index=Index([1, 2, "All"], name="a", dtype="object"),
    columns=Index([3, 4, "All"], name="b"),
)
test_case = crosstab(
    df.a, df.b, df.c, aggfunc="count", normalize="all", margins=True
)
tm.assert_frame_equal(test_case, norm_counts)

df = DataFrame(
    {"a": [1, 2, 2, 2, 2], "b": [3, 3, 4, 4, 4], "c": [0, 4, np.nan, 3, 3]}
)

norm_sum = DataFrame(
    [[0, 0, 0.0], [0.4, 0.6, 1], [0.4, 0.6, 1]],
    index=Index([1, 2, "All"], name="a", dtype="object"),
    columns=Index([3, 4, "All"], name="b", dtype="object"),
)
test_case = crosstab(
    df.a, df.b, df.c, aggfunc=np.sum, normalize="all", margins=True
)
tm.assert_frame_equal(test_case, norm_sum)
