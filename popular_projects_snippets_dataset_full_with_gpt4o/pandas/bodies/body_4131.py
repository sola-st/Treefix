# Extracted from ./data/repos/pandas/pandas/tests/frame/test_iteration.py
assert tm.equalContents(list(float_frame), float_frame.columns)
