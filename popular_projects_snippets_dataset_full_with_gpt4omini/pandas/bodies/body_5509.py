# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_arithmetic.py
val = Timestamp(1337299200000000123)
result = val + timedelta(1)
assert result.nanosecond == val.nanosecond
