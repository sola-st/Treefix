# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_constructors.py
with pytest.raises(ValueError, match="Cannot convert"):
    SparseArray([0, 1, np.nan], dtype=dtype)
