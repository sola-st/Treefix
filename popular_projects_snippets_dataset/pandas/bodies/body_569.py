# Extracted from ./data/repos/pandas/pandas/tests/dtypes/cast/test_promote.py
dtype = np.dtype(any_numpy_dtype)

# filling anything but timedelta with timedelta casts to object
if is_timedelta64_dtype(dtype):
    expected_dtype = dtype
    # for timedelta dtypes, scalar values get cast to pd.Timedelta.value
    exp_val_for_scalar = pd.Timedelta(fill_value).to_timedelta64()

    if isinstance(fill_value, np.timedelta64) and fill_value.dtype != "m8[ns]":
        mark = pytest.mark.xfail(
            reason="maybe_promote not yet updated to handle non-nano "
            "Timedelta scalar"
        )
        request.node.add_marker(mark)
    elif type(fill_value) is datetime.timedelta:
        mark = pytest.mark.xfail(
            reason="maybe_promote not yet updated to handle non-nano "
            "Timedelta scalar"
        )
        request.node.add_marker(mark)
else:
    expected_dtype = np.dtype(object)
    exp_val_for_scalar = fill_value

_check_promote(dtype, fill_value, expected_dtype, exp_val_for_scalar)
