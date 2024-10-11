# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_dtype.py
sparse_dtype = SparseDtype(dtype)
result = sparse_dtype.fill_value
if pd.isna(fill_value):
    assert pd.isna(result) and type(result) == type(fill_value)
else:
    assert result == fill_value
