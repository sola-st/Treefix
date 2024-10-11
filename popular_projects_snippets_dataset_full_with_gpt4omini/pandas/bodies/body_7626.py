# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_indexing.py
# GH#10645
result = MultiIndex.from_arrays([range(10**6), range(10**6)])
assert (10**6, 0) not in result
