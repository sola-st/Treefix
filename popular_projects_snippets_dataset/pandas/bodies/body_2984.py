# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_sort_values.py
# GH#45618
ser = pd.Series(Categorical(["a", "b", "a"], categories=["a", "b", "c"]))
df = pd.get_dummies(ser, dtype=dtype, sparse=True)

with tm.assert_produces_warning(None):
    # No warnings about constructing Index from SparseArray
    df.sort_values(by=df.columns.tolist())
