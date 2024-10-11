# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_arithmetic.py
# GH#6808
base = Timestamp("20130102 09:01:12.123456")
expected_add = Timestamp("20130103 09:01:22.123456")
expected_sub = Timestamp("20130101 09:01:02.123456")

result = base + one_day_ten_secs
assert result == expected_add

result = base - one_day_ten_secs
assert result == expected_sub
