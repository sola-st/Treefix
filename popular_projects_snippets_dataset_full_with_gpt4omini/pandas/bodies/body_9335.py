# Extracted from ./data/repos/pandas/pandas/tests/arrays/masked/test_arithmetic.py
data, scalar = data
op = tm.get_op_from_name(all_arithmetic_operators)
check_skip(data, all_arithmetic_operators)

scalar_array = pd.array([scalar] * len(data), dtype=data.dtype)

# TODO also add len-1 array (np.array([scalar], dtype=data.dtype.numpy_dtype))
for scalar in [scalar, data.dtype.type(scalar)]:
    if is_bool_not_implemented(data, all_arithmetic_operators):
        msg = "operator '.*' not implemented for bool dtypes"
        with pytest.raises(NotImplementedError, match=msg):
            op(data, scalar)
        with pytest.raises(NotImplementedError, match=msg):
            op(data, scalar_array)
    else:
        result = op(data, scalar)
        expected = op(data, scalar_array)
        tm.assert_extension_array_equal(result, expected)
