# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_constructors.py
result = Timestamp(datetime(2018, 1, 1), tz=tzutc())
expected = Timestamp(datetime(2018, 1, 1)).tz_localize(tzutc())
assert result == expected
