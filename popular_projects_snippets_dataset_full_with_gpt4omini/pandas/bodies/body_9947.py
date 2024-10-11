# Extracted from ./data/repos/pandas/pandas/tests/window/test_expanding.py
result = frame.expanding().corr()

rolling_result = frame.rolling(window=len(frame), min_periods=1).corr()
tm.assert_frame_equal(result, rolling_result)
