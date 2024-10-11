# Extracted from ./data/repos/pandas/pandas/tests/frame/test_nonunique_indexes.py

# assignment
# GH 3687
arr = np.random.randn(3, 2)
idx = list(range(2))
df = DataFrame(arr, columns=["A", "A"])
df.columns = idx
expected = DataFrame(arr, columns=idx)
check(df, expected)
