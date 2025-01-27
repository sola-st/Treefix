# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_common.py
# GH-44276
assert not com.is_dtype_equal(dtype, "string[pyarrow]")
