# Extracted from ./data/repos/pandas/pandas/tests/indexes/timedeltas/test_indexing.py
tdi = timedelta_range("1 day", periods=3, freq="D", name="idx")
cond = [True, True, False]
expected = TimedeltaIndex([tdi[0], tdi[1], tdi[0]], freq=None, name="idx")

result = tdi.where(cond, tdi[::-1])
tm.assert_index_equal(result, expected)
