# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_setops.py
# GH 46702: Europe/Berlin has DST transition
idx1 = date_range("2020-03-27", periods=5, freq="D", tz=tz)
idx2 = date_range("2020-03-30", periods=5, freq="D", tz=tz)
result = idx1.intersection(idx2)
expected = date_range("2020-03-30", periods=2, freq="D", tz=tz)
tm.assert_index_equal(result, expected)
