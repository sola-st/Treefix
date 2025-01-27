# Extracted from ./data/repos/pandas/pandas/tests/frame/test_unary.py
df = float_frame

tm.assert_frame_equal(-(df < 0), ~(df < 0))
