# Extracted from ./data/repos/pandas/pandas/tests/extension/test_sparse.py
arr = data_missing.take([1, 1])
df = pd.DataFrame({"A": arr}, copy=False)

filled_val = df.iloc[0, 0]
result = df.fillna(filled_val)

if hasattr(df._mgr, "blocks"):
    assert df.values.base is not result.values.base
assert df.A._values.to_dense() is arr.to_dense()
