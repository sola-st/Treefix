# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_dtypes.py
assert CategoricalDtype.is_dtype(dtype)
assert CategoricalDtype.is_dtype("category")
assert CategoricalDtype.is_dtype(CategoricalDtype())
assert not CategoricalDtype.is_dtype("foo")
assert not CategoricalDtype.is_dtype(np.float64)
