# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_series.py
# ensure names argument is not ignored on axis=1, #23490
s = Series([1, 2, 3])
s2 = Series([4, 5, 6])
result = concat([s, s2], axis=1, keys=["a", "b"], names=["A"])
expected = DataFrame(
    [[1, 4], [2, 5], [3, 6]], columns=Index(["a", "b"], name="A")
)
tm.assert_frame_equal(result, expected)

result = concat([s, s2], axis=1, keys=[("a", 1), ("b", 2)], names=["A", "B"])
expected = DataFrame(
    [[1, 4], [2, 5], [3, 6]],
    columns=MultiIndex.from_tuples([("a", 1), ("b", 2)], names=["A", "B"]),
)
tm.assert_frame_equal(result, expected)
