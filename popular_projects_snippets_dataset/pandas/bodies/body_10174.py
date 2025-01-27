# Extracted from ./data/repos/pandas/pandas/tests/window/test_groupby.py
# a few different cases checking the created MultiIndex of the result
# https://github.com/pandas-dev/pandas/pull/38057

# grouping by 1 columns -> 2-level MI as result
df = DataFrame({"a": np.arange(8.0), "b": [1, 2] * 4})
result = df.groupby("b").rolling(3).mean()
expected_index = MultiIndex.from_tuples(
    [(1, 0), (1, 2), (1, 4), (1, 6), (2, 1), (2, 3), (2, 5), (2, 7)],
    names=["b", None],
)
tm.assert_index_equal(result.index, expected_index)
