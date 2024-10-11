# Extracted from ./data/repos/pandas/pandas/tests/indexes/timedeltas/test_setops.py

i1 = timedelta_range("1day", periods=5)
i2 = timedelta_range("3day", periods=5)
result = i1.union(i2)
expected = timedelta_range("1day", periods=7)
tm.assert_index_equal(result, expected)

i1 = Index(np.arange(0, 20, 2, dtype=np.int64))
i2 = timedelta_range(start="1 day", periods=10, freq="D")
i1.union(i2)  # Works
i2.union(i1)  # Fails with "AttributeError: can't set attribute"
