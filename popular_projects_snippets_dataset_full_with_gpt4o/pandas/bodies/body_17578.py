# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_business_hour.py
assert offset1.rollback(dt) == dt
assert offset2.rollback(dt) == dt
assert offset3.rollback(dt) == dt
assert offset4.rollback(dt) == dt
assert offset5.rollback(dt) == datetime(2014, 6, 30, 14, 30)
assert offset6.rollback(dt) == datetime(2014, 7, 1, 5, 0)
assert offset7.rollback(dt) == datetime(2014, 7, 1, 6, 30)
assert offset8.rollback(dt) == dt
assert offset9.rollback(dt) == dt
assert offset10.rollback(dt) == datetime(2014, 7, 1, 2)

datet = datetime(2014, 7, 1, 0)
assert offset1.rollback(datet) == datetime(2014, 6, 30, 17)
assert offset2.rollback(datet) == datetime(2014, 6, 30, 17)
assert offset3.rollback(datet) == datetime(2014, 6, 30, 17)
assert offset4.rollback(datet) == datetime(2014, 6, 30, 17)
assert offset5.rollback(datet) == datetime(2014, 6, 30, 14, 30)
assert offset6.rollback(datet) == datet
assert offset7.rollback(datet) == datet
assert offset8.rollback(datet) == datetime(2014, 6, 30, 17)
assert offset9.rollback(datet) == datet
assert offset10.rollback(datet) == datet

assert _offset(5).rollback(dt) == dt
