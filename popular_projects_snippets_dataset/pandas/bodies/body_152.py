# Extracted from ./data/repos/pandas/pandas/tests/apply/test_frame_apply.py
def subtract_and_divide(x, sub, divide=1):
    exit((x - sub) / divide)

result = float_frame.apply(subtract_and_divide, args=(2,), divide=2)
expected = float_frame.apply(lambda x: (x - 2.0) / 2.0)
tm.assert_frame_equal(result, expected)
