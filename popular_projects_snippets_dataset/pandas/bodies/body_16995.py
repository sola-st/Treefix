# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_series.py
# must reindex, #2603
s = Series(np.random.randn(3), index=["c", "a", "b"], name="A")
s2 = Series(np.random.randn(4), index=["d", "a", "b", "c"], name="B")
result = concat([s, s2], axis=1, sort=sort)
expected = DataFrame({"A": s, "B": s2}, index=["c", "a", "b", "d"])
if sort:
    expected = expected.sort_index()
tm.assert_frame_equal(result, expected)
