# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
# empty dict plus index
idx = Index([0, 1, 2])
frame = DataFrame({}, index=idx)
assert frame.index is idx
