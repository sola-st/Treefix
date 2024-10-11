# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_join.py
# GH#46850
# Join a DataFrame with a list containing both a Series and a DataFrame
left = float_frame.A.to_frame()
right = [float_frame.B, float_frame[["C", "D"]]]
result = left.join(right)
tm.assert_frame_equal(result, float_frame)
