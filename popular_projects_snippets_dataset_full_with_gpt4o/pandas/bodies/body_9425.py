# Extracted from ./data/repos/pandas/pandas/tests/arrays/integer/test_arithmetic.py
left = pd.array([1, None, 3, 4], dtype=dtype)
right = pd.array([None, 3, 5, 4], dtype=dtype)

result = left | right
expected = pd.array([None, None, 3 | 5, 4 | 4], dtype=dtype)
tm.assert_extension_array_equal(result, expected)

result = left & right
expected = pd.array([None, None, 3 & 5, 4 & 4], dtype=dtype)
tm.assert_extension_array_equal(result, expected)

result = left ^ right
expected = pd.array([None, None, 3 ^ 5, 4 ^ 4], dtype=dtype)
tm.assert_extension_array_equal(result, expected)

# TODO: desired behavior when operating with boolean?  defer?

floats = right.astype("Float64")
with pytest.raises(TypeError, match="unsupported operand type"):
    left | floats
with pytest.raises(TypeError, match="unsupported operand type"):
    left & floats
with pytest.raises(TypeError, match="unsupported operand type"):
    left ^ floats
