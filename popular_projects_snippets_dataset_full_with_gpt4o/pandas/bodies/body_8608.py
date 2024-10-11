# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_join.py
index = date_range("1/1/2000", periods=10)
joined = index.join(index, how=join_type)
assert index is joined
