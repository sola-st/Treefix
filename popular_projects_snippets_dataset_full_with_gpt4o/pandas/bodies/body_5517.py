# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_arithmetic.py
# GH#24775 timedelta64+Timestamp should not raise
ts = fixed_now_ts
assert td + ts == ts + td
