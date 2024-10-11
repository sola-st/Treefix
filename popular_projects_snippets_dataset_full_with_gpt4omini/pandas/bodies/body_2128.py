# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
# GH 17697, 11736
ts_str = "2015-11-18 15:30:00+05:30"
result = to_datetime(ts_str)
expected = Timestamp(ts_str)
assert result == expected

expected = DatetimeIndex([Timestamp(ts_str)] * 2)
result = to_datetime([ts_str] * 2)
tm.assert_index_equal(result, expected)

result = DatetimeIndex([ts_str] * 2)
tm.assert_index_equal(result, expected)
