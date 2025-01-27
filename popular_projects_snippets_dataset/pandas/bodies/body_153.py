# Extracted from ./data/repos/pandas/pandas/tests/apply/test_frame_apply.py
result = float_frame.apply(list)
tm.assert_frame_equal(result, float_frame)
