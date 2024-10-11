# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_dtypes.py
result = is_bool_dtype(Series(SparseArray([True, False])))
assert result is True
