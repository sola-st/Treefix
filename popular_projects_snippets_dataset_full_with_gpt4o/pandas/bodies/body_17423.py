# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_custom_business_hour.py
assert offset1.rollback(dt) == dt
assert offset2.rollback(dt) == dt

d = datetime(2014, 7, 1, 0)

# 2014/07/01 is Tuesday, 06/30 is Monday(holiday)
assert offset1.rollback(d) == datetime(2014, 6, 27, 17)

# 2014/6/30 and 2014/6/27 are holidays
assert offset2.rollback(d) == datetime(2014, 6, 26, 17)
