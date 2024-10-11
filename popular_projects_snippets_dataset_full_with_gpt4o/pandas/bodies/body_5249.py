# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_timedelta.py
# GH 31354
td = Timedelta(1552211999999999872, unit="ns")
result = td.days * 86400
result += td.seconds
result *= 1000000
result += td.microseconds
result *= 1000
result += td.nanoseconds
expected = td.value
assert result == expected
