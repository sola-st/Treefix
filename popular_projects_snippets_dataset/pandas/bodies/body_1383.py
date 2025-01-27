# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_iloc.py
df = DataFrame(
    np.arange(8, dtype=np.int64).reshape(2, 4), columns=["A", "B", "A", "B"]
)
df.iloc[:, 0] = df.iloc[:, 0].astype(np.float64)
assert df.dtypes.iloc[2] == np.int64
