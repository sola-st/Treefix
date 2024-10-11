# Extracted from ./data/repos/pandas/pandas/tests/frame/test_arithmetic.py
f = getattr(operator, op)

# vs mix int
result = getattr(mixed_int_frame, op)(2 + mixed_int_frame)
expected = f(mixed_int_frame, 2 + mixed_int_frame)

# no overflow in the uint
dtype = None
if op in ["__sub__"]:
    dtype = {"B": "uint64", "C": None}
elif op in ["__add__", "__mul__"]:
    dtype = {"C": None}
if expr.USE_NUMEXPR and switch_numexpr_min_elements == 0:
    # when using numexpr, the casting rules are slightly different:
    # in the `2 + mixed_int_frame` operation, int32 column becomes
    # and int64 column (not preserving dtype in operation with Python
    # scalar), and then the int32/int64 combo results in int64 result
    dtype["A"] = (2 + mixed_int_frame)["A"].dtype
tm.assert_frame_equal(result, expected)
_check_mixed_int(result, dtype=dtype)

# vs mix float
result = getattr(mixed_float_frame, op)(2 * mixed_float_frame)
expected = f(mixed_float_frame, 2 * mixed_float_frame)
tm.assert_frame_equal(result, expected)
_check_mixed_float(result, dtype={"C": None})

# vs plain int
result = getattr(int_frame, op)(2 * int_frame)
expected = f(int_frame, 2 * int_frame)
tm.assert_frame_equal(result, expected)
