# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_interval.py
# GH 19209
left = np.arange(0, 4, dtype="i8")
right = np.arange(1, 5, dtype="i8")

result = IntervalIndex.from_arrays(left, right).nbytes
expected = 64  # 4 * 8 * 2
assert result == expected
