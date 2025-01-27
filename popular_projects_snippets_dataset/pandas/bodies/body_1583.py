# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# Test with np.inf in columns
df = DataFrame()
df.loc[0, 0] = 1
df.loc[1, 1] = 2
df.loc[0, np.inf] = 3

result = df.columns
expected = Index([0, 1, np.inf], dtype=np.float64)
tm.assert_index_equal(result, expected)
