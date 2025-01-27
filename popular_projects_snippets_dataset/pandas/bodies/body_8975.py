# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_astype.py
arr = SparseArray([1.0, np.nan])
with pytest.raises(ValueError, match="Cannot convert non-finite"):
    arr.astype(int)
