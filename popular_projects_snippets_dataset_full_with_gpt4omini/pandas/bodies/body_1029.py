# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_partial.py
# gh-12660
iterables = [["a", "b"], [2, 1]]
columns = MultiIndex.from_product(iterables, names=["col1", "col2"])
rows = MultiIndex.from_product(iterables, names=["row1", "row2"])
df = DataFrame(np.random.randn(4, 4), index=rows, columns=columns)
expected = df.iloc[:2, 2:].droplevel("row1").droplevel("col1", axis=1)
result = df.loc["a", "b"]
tm.assert_frame_equal(result, expected)
