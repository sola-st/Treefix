# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_date_range.py
# GH49441
result = date_range(start=start, periods=period, freq="C")
expected = DatetimeIndex(expected)
tm.assert_index_equal(result, expected)
