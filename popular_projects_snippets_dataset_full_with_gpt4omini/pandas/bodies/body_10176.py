# Extracted from ./data/repos/pandas/pandas/tests/window/test_groupby.py
# grouping with 1 level on dataframe with 2-level MI -> 3-level MI as result
df = DataFrame({"a": np.arange(8.0), "b": [1, 2] * 4, "c": [1, 2, 3, 4] * 2})
df = df.set_index("c", append=True)
result = df.groupby("b").rolling(3).mean()
expected_index = MultiIndex.from_tuples(
    [
        (1, 0, 1),
        (1, 2, 3),
        (1, 4, 1),
        (1, 6, 3),
        (2, 1, 2),
        (2, 3, 4),
        (2, 5, 2),
        (2, 7, 4),
    ],
    names=["b", None, "c"],
)
tm.assert_index_equal(result.index, expected_index, exact="equiv")
