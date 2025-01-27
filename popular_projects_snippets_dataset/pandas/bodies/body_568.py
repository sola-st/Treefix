# Extracted from ./data/repos/pandas/pandas/tests/dtypes/cast/test_promote.py
dtype = np.dtype(timedelta64_dtype)
fill_dtype = np.dtype(any_numpy_dtype)

# create array of given dtype; casts "1" to correct dtype
fill_value = np.array([1], dtype=fill_dtype)[0]

# filling timedelta with anything but timedelta casts to object
if is_timedelta64_dtype(fill_dtype):
    expected_dtype = dtype
    # for timedelta dtypes, scalar values get cast to pd.Timedelta.value
    exp_val_for_scalar = pd.Timedelta(fill_value).to_timedelta64()
else:
    expected_dtype = np.dtype(object)
    exp_val_for_scalar = fill_value

_check_promote(dtype, fill_value, expected_dtype, exp_val_for_scalar)
