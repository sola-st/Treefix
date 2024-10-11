# Extracted from ./data/repos/pandas/pandas/tests/indexes/timedeltas/test_join.py
# GH#32157
tdi = timedelta_range("1 day", periods=10)
result = tdi[:5].join(tdi[5:], how="outer")
assert result.freq == tdi.freq
tm.assert_index_equal(result, tdi)

result = tdi[:5].join(tdi[6:], how="outer")
assert result.freq is None
expected = tdi.delete(5)
tm.assert_index_equal(result, expected)
