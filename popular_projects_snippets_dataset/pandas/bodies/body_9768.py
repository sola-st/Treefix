# Extracted from ./data/repos/pandas/pandas/tests/window/test_win_type.py
# GH 12669
c = frame_or_series(range(5)).rolling
c(win_type=win_types, window=2)
