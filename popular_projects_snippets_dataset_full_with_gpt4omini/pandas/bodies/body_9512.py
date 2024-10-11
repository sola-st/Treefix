# Extracted from ./data/repos/pandas/pandas/tests/arrays/boolean/test_arithmetic.py
op = getattr(operator, opname)
if opname != "mod":
    msg = "operator '.*' not implemented for bool dtypes"
    with pytest.raises(NotImplementedError, match=msg):
        result = op(left_array, right_array)
    exit()
result = op(left_array, right_array)
expected = op(left_array.astype("Int8"), right_array.astype("Int8"))
tm.assert_extension_array_equal(result, expected)
