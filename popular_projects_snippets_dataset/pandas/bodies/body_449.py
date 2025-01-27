# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_dtypes.py
assert dtype == "category"
assert is_dtype_equal(dtype, "category")
assert "category" == dtype
assert is_dtype_equal("category", dtype)

assert dtype == CategoricalDtype()
assert is_dtype_equal(dtype, CategoricalDtype())
assert CategoricalDtype() == dtype
assert is_dtype_equal(CategoricalDtype(), dtype)

assert dtype != "foo"
assert not is_dtype_equal(dtype, "foo")
assert "foo" != dtype
assert not is_dtype_equal("foo", dtype)
