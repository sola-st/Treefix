# Extracted from ./data/repos/pandas/pandas/tests/indexes/timedeltas/test_indexing.py
tdi = timedelta_range("1 day", periods=3, freq="D", name="idx")
cond = np.array([True, False, False])

dtnat = np.datetime64("NaT", "ns")
expected = Index([tdi[0], dtnat, dtnat], dtype=object, name="idx")
assert expected[2] is dtnat
result = tdi.where(cond, dtnat)
tm.assert_index_equal(result, expected)
