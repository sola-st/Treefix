# Extracted from ./data/repos/pandas/pandas/tests/indexes/ranges/test_join.py
index = RangeIndex(start=0, stop=20, step=2)
joined = index.join(index, how=join_type)
assert index is joined
