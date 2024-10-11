# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_dtypes.py
a = CategoricalDtype(["a", "b", 1, 2])
b = CategoricalDtype(["a", "b", "1", "2"])
assert hash(a) != hash(b)
