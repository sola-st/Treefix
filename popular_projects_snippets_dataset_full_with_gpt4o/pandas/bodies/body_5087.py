# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_arithmetic.py
# GH#6808
base = Timestamp("20130101 09:01:12.123456")
expected_add = Timestamp("20130101 09:01:22.123456")
expected_sub = Timestamp("20130101 09:01:02.123456")

result = base + ten_seconds
assert result == expected_add

result = base - ten_seconds
assert result == expected_sub
