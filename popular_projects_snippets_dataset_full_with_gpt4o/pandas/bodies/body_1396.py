# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_indexing.py
# GH 16957
# We should be able to use np.inf as a key
# np.inf should cause an index to convert to float

# Test with np.inf in rows
df = DataFrame(columns=[0])
df.loc[1] = 1
df.loc[2] = 2
df.loc[np.inf] = 3

# make sure we can look up the value
assert df.loc[np.inf, 0] == 3

result = df.index
expected = Index([1, 2, np.inf], dtype=np.float64)
tm.assert_index_equal(result, expected)
