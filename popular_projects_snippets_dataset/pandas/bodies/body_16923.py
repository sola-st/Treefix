# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_append.py
empty = DataFrame()

appended = float_frame._append(empty)
tm.assert_frame_equal(float_frame, appended)
assert appended is not float_frame

appended = empty._append(float_frame)
tm.assert_frame_equal(float_frame, appended)
assert appended is not float_frame
