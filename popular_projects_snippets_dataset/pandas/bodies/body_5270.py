# Extracted from ./data/repos/pandas/pandas/tests/scalar/period/test_period.py
# Issue #36430
# Integer overflow for Period over the maximum timestamp
p = Period(ordinal=2562048 + hour, freq="1H")
assert p.hour == hour
