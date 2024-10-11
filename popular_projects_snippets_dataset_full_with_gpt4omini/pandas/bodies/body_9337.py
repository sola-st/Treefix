# Extracted from ./data/repos/pandas/pandas/tests/arrays/masked/test_arithmetic.py
data, scalar = data
op = tm.get_op_from_name(all_arithmetic_operators)
check_skip(data, all_arithmetic_operators)

numpy_array = np.array([scalar] * len(data), dtype=data.dtype.numpy_dtype)
pd_array = pd.array(numpy_array, dtype=data.dtype)

if is_bool_not_implemented(data, all_arithmetic_operators):
    msg = "operator '.*' not implemented for bool dtypes"
    with pytest.raises(NotImplementedError, match=msg):
        op(data, numpy_array)
    with pytest.raises(NotImplementedError, match=msg):
        op(data, pd_array)
    exit()

result = op(data, numpy_array)
expected = op(data, pd_array)
tm.assert_extension_array_equal(result, expected)
