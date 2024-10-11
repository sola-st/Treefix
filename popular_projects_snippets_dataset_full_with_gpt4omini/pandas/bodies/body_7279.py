# Extracted from ./data/repos/pandas/pandas/tests/indexes/timedeltas/methods/test_insert.py
idx = timedelta_range("1day", "3day")

result = idx.insert(0, "1 Day")

expected = TimedeltaIndex([idx[0]] + list(idx))
tm.assert_index_equal(result, expected)
