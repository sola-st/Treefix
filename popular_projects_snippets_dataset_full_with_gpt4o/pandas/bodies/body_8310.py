# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_setops.py
i1 = Index(np.arange(0, 20, 2, dtype=np.int64))
i2 = date_range(start="2012-01-03 00:00:00", periods=10, freq="D")
# Works
i1.union(i2, sort=sort)
# Fails with "AttributeError: can't set attribute"
i2.union(i1, sort=sort)
