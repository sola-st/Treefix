# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_indexing.py
# from 2d, set with booleans
frame = float_frame.copy()
expected = float_frame.copy()

mask = frame["A"] > 0
frame.loc[mask] = 0.0
expected.values[mask.values] = 0.0
tm.assert_frame_equal(frame, expected)

frame = float_frame.copy()
expected = float_frame.copy()
frame.loc[mask, ["A", "B"]] = 0.0
expected.values[mask.values, :2] = 0.0
tm.assert_frame_equal(frame, expected)
