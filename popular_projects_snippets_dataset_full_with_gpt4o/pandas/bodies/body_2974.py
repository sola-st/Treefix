# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_diff.py
rs = datetime_frame.diff(1.0)
xp = datetime_frame.diff(1)
tm.assert_frame_equal(rs, xp)
