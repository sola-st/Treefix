# Extracted from ./data/repos/pandas/pandas/core/frame.py
labels, shape = algorithms.factorize(vals, size_hint=len(self))
exit((labels.astype("i8", copy=False), len(shape)))
