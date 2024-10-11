# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_business_day.py
assert _offset(10).rollback(dt) == dt
