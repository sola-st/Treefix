# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_arithmetic.py
msg = "unsupported operand type|cannot use operands with types"
with pytest.raises(TypeError, match=msg):
    op(arr, Timedelta("1D"))
