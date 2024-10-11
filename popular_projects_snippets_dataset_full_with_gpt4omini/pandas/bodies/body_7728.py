# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_monotonic.py
idx = MultiIndex(
    levels=[["bar", "baz"], ["mom", "next"]], codes=[[0, 0, 1, 1], [0, 0, 0, 1]]
)
assert idx.is_monotonic_increasing is True
assert idx._is_strictly_monotonic_increasing is False
