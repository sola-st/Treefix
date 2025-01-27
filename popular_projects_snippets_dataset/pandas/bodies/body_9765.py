# Extracted from ./data/repos/pandas/pandas/tests/window/test_win_type.py
# GH 12669
c = frame_or_series(range(5)).rolling

# valid
c(win_type="boxcar", window=2, min_periods=1)
c(win_type="boxcar", window=2, min_periods=1, center=True)
c(win_type="boxcar", window=2, min_periods=1, center=False)
