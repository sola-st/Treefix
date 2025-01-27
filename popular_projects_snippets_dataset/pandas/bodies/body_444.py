# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_dtypes.py
assert not dtype == "foo"
assert not is_dtype_equal(dtype, np.int64)
