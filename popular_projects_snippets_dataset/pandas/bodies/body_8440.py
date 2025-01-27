# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_date_range.py
result = bdate_range("2013-05-01", periods=3, freq="C")
expected = DatetimeIndex(["2013-05-01", "2013-05-02", "2013-05-03"], freq="C")
tm.assert_index_equal(result, expected)
assert result.freq == expected.freq
