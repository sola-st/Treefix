# Extracted from ./data/repos/pandas/pandas/tests/indexes/ranges/test_range.py

# memory savings vs int index
idx = RangeIndex(0, 1000)
assert idx.nbytes < Index(idx._values).nbytes / 10

# constant memory usage
i2 = RangeIndex(0, 10)
assert idx.nbytes == i2.nbytes
