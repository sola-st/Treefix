# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_reindex.py
# based on asv time_reindex_axis1
N = 10
df = DataFrame(np.random.randn(N * 10, N))
cols = np.arange(N)
np.random.shuffle(cols)

result = df.reindex(columns=cols, copy=True)
assert not np.shares_memory(result[0]._values, df[0]._values)

# pass both columns and index
result2 = df.reindex(columns=cols, index=df.index, copy=True)
assert not np.shares_memory(result2[0]._values, df[0]._values)
