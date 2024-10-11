# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_diff.py
rs = datetime_frame.diff(-1)
xp = datetime_frame - datetime_frame.shift(-1)
tm.assert_frame_equal(rs, xp)
