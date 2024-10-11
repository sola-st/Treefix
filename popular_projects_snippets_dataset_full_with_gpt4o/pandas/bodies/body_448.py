# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_dtypes.py
dtype2 = CategoricalDtype()
assert dtype == dtype2
assert dtype2 == dtype
assert hash(dtype) == hash(dtype2)
