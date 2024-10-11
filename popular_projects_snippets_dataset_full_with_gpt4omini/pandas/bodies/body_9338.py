# Extracted from ./data/repos/pandas/pandas/tests/arrays/masked/test_arithmetic.py
data, scalar = data
op = tm.get_op_from_name(all_arithmetic_operators)
check_skip(data, all_arithmetic_operators)

# DataFrame with scalar
df = pd.DataFrame({"A": data})

if is_bool_not_implemented(data, all_arithmetic_operators):
    msg = "operator '.*' not implemented for bool dtypes"
    with pytest.raises(NotImplementedError, match=msg):
        op(df, scalar)
    with pytest.raises(NotImplementedError, match=msg):
        op(data, scalar)
    exit()

result = op(df, scalar)
expected = pd.DataFrame({"A": op(data, scalar)})
tm.assert_frame_equal(result, expected)
