# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
# make sure we handle out-of-bounds *before*
# constructing the dates

result = to_datetime(arg, unit="D", origin=origin)
expected = Timestamp(expected_str)
assert result == expected

result = to_datetime(200 * 365, unit="D", origin="1870-01-01")
expected = Timestamp("2069-11-13 00:00:00")
assert result == expected

result = to_datetime(300 * 365, unit="D", origin="1870-01-01")
expected = Timestamp("2169-10-20 00:00:00")
assert result == expected
