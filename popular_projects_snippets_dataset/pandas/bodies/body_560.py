# Extracted from ./data/repos/pandas/pandas/tests/dtypes/cast/test_promote.py

dtype = np.dtype(dtype)
expected_dtype = np.dtype(expected_dtype)

# output is not a generic float, but corresponds to expected_dtype
exp_val_for_scalar = np.array([fill_value], dtype=expected_dtype)[0]

_check_promote(dtype, fill_value, expected_dtype, exp_val_for_scalar)
