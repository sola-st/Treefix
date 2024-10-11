# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_explode.py
s = pd.Series(
    [[0, 1, 2], np.nan, [], (3, 4)],
    name="foo",
    index=pd.MultiIndex.from_product([list("ab"), range(2)], names=["foo", "bar"]),
)
result = s.explode()
index = pd.MultiIndex.from_tuples(
    [("a", 0), ("a", 0), ("a", 0), ("a", 1), ("b", 0), ("b", 1), ("b", 1)],
    names=["foo", "bar"],
)
expected = pd.Series(
    [0, 1, 2, np.nan, np.nan, 3, 4], index=index, dtype=object, name="foo"
)
tm.assert_series_equal(result, expected)
