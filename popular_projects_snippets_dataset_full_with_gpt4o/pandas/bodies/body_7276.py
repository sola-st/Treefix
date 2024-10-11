# Extracted from ./data/repos/pandas/pandas/tests/indexes/timedeltas/methods/test_insert.py
# GH 18295 (test missing)
idx = timedelta_range("1day", "3day")
result = idx.insert(1, null)
expected = TimedeltaIndex(["1day", pd.NaT, "2day", "3day"])
tm.assert_index_equal(result, expected)
