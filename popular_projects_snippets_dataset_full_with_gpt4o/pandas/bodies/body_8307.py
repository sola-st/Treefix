# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_setops.py
# GH11086
expected = bdate_range("20150101", periods=10)
expected._data.freq = None

result = expected.union(expected, sort=sort)
tm.assert_index_equal(result, expected)
assert result.freq is None
