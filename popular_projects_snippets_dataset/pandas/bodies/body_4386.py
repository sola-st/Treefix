# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
# empty dict with index and columns
idx = Index([0, 1, 2])
frame = DataFrame({}, index=idx, columns=idx)
assert frame.index is idx
assert frame.columns is idx
assert len(frame._series) == 3
