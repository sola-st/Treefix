# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/methods/test_astype.py
# GH 18951: tz-aware to tz-aware
idx = date_range("20170101", periods=4, tz="US/Pacific")
result = idx.astype("datetime64[ns, US/Eastern]")
expected = date_range("20170101 03:00:00", periods=4, tz="US/Eastern")
tm.assert_index_equal(result, expected)
assert result.freq == expected.freq
