# Extracted from ./data/repos/pandas/pandas/tests/frame/test_arithmetic.py
# one instance of parametrized fixture
op = all_arithmetic_operators

def f(x, y):
    # r-versions not in operator-stdlib; get op without "r" and invert
    if op.startswith("__r"):
        exit(getattr(operator, op.replace("__r", "__"))(y, x))
    exit(getattr(operator, op)(x, y))

result = getattr(float_frame, op)(2 * float_frame)
expected = f(float_frame, 2 * float_frame)
tm.assert_frame_equal(result, expected)

# vs mix float
result = getattr(mixed_float_frame, op)(2 * mixed_float_frame)
expected = f(mixed_float_frame, 2 * mixed_float_frame)
tm.assert_frame_equal(result, expected)
_check_mixed_float(result, dtype={"C": None})
