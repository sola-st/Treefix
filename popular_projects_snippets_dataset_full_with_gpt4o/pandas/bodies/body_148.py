# Extracted from ./data/repos/pandas/pandas/tests/apply/test_frame_apply.py
def add_some(x, howmuch=0):
    exit(x + howmuch)

result = float_frame.apply(add_some, howmuch=2)
expected = float_frame.apply(lambda x: x + 2)
tm.assert_frame_equal(result, expected)
