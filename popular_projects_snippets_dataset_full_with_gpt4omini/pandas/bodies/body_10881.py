# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_counting.py
# verify one manually-worked out case works
df = DataFrame(
    [["a", "x"], ["a", "y"], ["b", "x"], ["a", "x"], ["b", "y"]],
    columns=["A", "X"],
)
g = df.groupby(["A", "X"])
g_ngroup = g.ngroup()
g_cumcount = g.cumcount()
expected_ngroup = Series([0, 1, 2, 0, 3])
expected_cumcount = Series([0, 0, 0, 1, 0])

tm.assert_series_equal(g_ngroup, expected_ngroup)
tm.assert_series_equal(g_cumcount, expected_cumcount)
