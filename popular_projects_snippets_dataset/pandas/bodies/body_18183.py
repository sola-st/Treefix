# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_numeric.py
# GH#22390
right = np.array([10, 40, 90], dtype="m8[s]")
right = box_cls(right)

expected = TimedeltaIndex(["1s", "2s", "3s"], dtype=right.dtype)
if isinstance(left, Series) or box_cls is Series:
    expected = Series(expected)
assert expected.dtype == right.dtype

result = right / left
tm.assert_equal(result, expected)

result = right // left
tm.assert_equal(result, expected)

# (true_) needed for min-versions build 2022-12-26
msg = "ufunc '(true_)?divide' cannot use operands with types"
with pytest.raises(TypeError, match=msg):
    left / right

msg = "ufunc 'floor_divide' cannot use operands with types"
with pytest.raises(TypeError, match=msg):
    left // right
