# Extracted from ./data/repos/pandas/pandas/tests/dtypes/cast/test_promote.py
dtype = np.dtype(datetime64_dtype)
fill_dtype = np.dtype(any_numpy_dtype)

# create array of given dtype; casts "1" to correct dtype
fill_value = np.array([1], dtype=fill_dtype)[0]

# filling datetime with anything but datetime casts to object
if is_datetime64_dtype(fill_dtype):
    expected_dtype = dtype
    # for datetime dtypes, scalar values get cast to to_datetime64
    exp_val_for_scalar = pd.Timestamp(fill_value).to_datetime64()
else:
    expected_dtype = np.dtype(object)
    exp_val_for_scalar = fill_value

_check_promote(dtype, fill_value, expected_dtype, exp_val_for_scalar)
