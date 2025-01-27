# Extracted from ./data/repos/pandas/pandas/tests/arrays/masked/test_arithmetic.py
data, scalar = data
op = tm.get_op_from_name(all_arithmetic_operators)
check_skip(data, all_arithmetic_operators)

ser = pd.Series(data)

others = [
    scalar,
    np.array([scalar] * len(data), dtype=data.dtype.numpy_dtype),
    pd.array([scalar] * len(data), dtype=data.dtype),
    pd.Series([scalar] * len(data), dtype=data.dtype),
]

for other in others:
    if is_bool_not_implemented(data, all_arithmetic_operators):
        msg = "operator '.*' not implemented for bool dtypes"
        with pytest.raises(NotImplementedError, match=msg):
            op(ser, other)

    else:
        result = op(ser, other)
        expected = pd.Series(op(data, other))
        tm.assert_series_equal(result, expected)
