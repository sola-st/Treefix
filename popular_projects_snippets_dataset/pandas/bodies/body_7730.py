# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_monotonic.py
# GH: 37220
idx = MultiIndex.from_tuples(values, names=["test"])
assert getattr(idx, attr) is False
