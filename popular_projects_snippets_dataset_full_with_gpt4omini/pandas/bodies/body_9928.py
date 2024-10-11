# Extracted from ./data/repos/pandas/pandas/tests/window/test_expanding.py
# GH 12669

c = frame_or_series(range(5)).expanding

# valid
c(min_periods=1)
