# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_indexing.py
d = datetime(2011, 12, 5, 20, 30)
ix = DatetimeIndex([d, d])
assert d in ix
