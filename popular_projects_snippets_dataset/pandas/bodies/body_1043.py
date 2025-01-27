# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_iloc.py
# GH 1678
columns = MultiIndex.from_tuples(
    [("Ohio", "Green"), ("Ohio", "Red"), ("Colorado", "Green")]
)
index = MultiIndex.from_tuples([("a", 1), ("a", 2), ("b", 1), ("b", 2)])

df = DataFrame(np.arange(12).reshape((4, 3)), index=index, columns=columns)

result = df.iloc[:, 1]
expected = df.loc[:, ("Ohio", "Red")]
tm.assert_series_equal(result, expected)
