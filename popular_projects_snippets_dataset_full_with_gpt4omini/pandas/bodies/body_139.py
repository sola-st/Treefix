# Extracted from ./data/repos/pandas/pandas/tests/apply/test_frame_apply.py
# no reduction
result = float_frame.apply(lambda x: x * 2, raw=True)
expected = float_frame * 2
tm.assert_frame_equal(result, expected)
