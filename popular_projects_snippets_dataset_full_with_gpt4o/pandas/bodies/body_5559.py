# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_constructors.py
# GH 30395
expected_timestamp = Timestamp("2000-01-03 00:00:00")
expected_stdlib = datetime.fromisocalendar(2000, 1, 1)
result = Timestamp.fromisocalendar(2000, 1, 1)
assert result == expected_timestamp
assert result == expected_stdlib
assert isinstance(result, Timestamp)
