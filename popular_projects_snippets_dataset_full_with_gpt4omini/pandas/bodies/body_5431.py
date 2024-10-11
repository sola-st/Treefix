# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_timestamp.py
ts = Timestamp("2013-05-01 07:15:45.123456789")
# GH 7878
expected_repr = "2013-05-01 07:15:45.123456789"
expected_value = 1_367_392_545_123_456_789
assert ts.value == expected_value
assert expected_repr in repr(ts)

ts = Timestamp("2013-05-01 07:15:45.123456789+09:00", tz="Asia/Tokyo")
assert ts.value == expected_value - 9 * 3600 * 1_000_000_000
assert expected_repr in repr(ts)

ts = Timestamp("2013-05-01 07:15:45.123456789", tz="UTC")
assert ts.value == expected_value
assert expected_repr in repr(ts)

ts = Timestamp("2013-05-01 07:15:45.123456789", tz="US/Eastern")
assert ts.value == expected_value + 4 * 3600 * 1_000_000_000
assert expected_repr in repr(ts)

# GH 10041
ts = Timestamp("20130501T071545.123456789")
assert ts.value == expected_value
assert expected_repr in repr(ts)
