# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_business_hour.py
assert offset1.rollforward(dt) == dt
assert offset2.rollforward(dt) == dt
assert offset3.rollforward(dt) == dt
assert offset4.rollforward(dt) == dt
assert offset5.rollforward(dt) == datetime(2014, 7, 1, 11, 0)
assert offset6.rollforward(dt) == datetime(2014, 7, 1, 20, 0)
assert offset7.rollforward(dt) == datetime(2014, 7, 1, 21, 30)
assert offset8.rollforward(dt) == dt
assert offset9.rollforward(dt) == dt
assert offset10.rollforward(dt) == datetime(2014, 7, 1, 13)

datet = datetime(2014, 7, 1, 0)
assert offset1.rollforward(datet) == datetime(2014, 7, 1, 9)
assert offset2.rollforward(datet) == datetime(2014, 7, 1, 9)
assert offset3.rollforward(datet) == datetime(2014, 7, 1, 9)
assert offset4.rollforward(datet) == datetime(2014, 7, 1, 9)
assert offset5.rollforward(datet) == datetime(2014, 7, 1, 11)
assert offset6.rollforward(datet) == datet
assert offset7.rollforward(datet) == datet
assert offset8.rollforward(datet) == datetime(2014, 7, 1, 9)
assert offset9.rollforward(datet) == datet
assert offset10.rollforward(datet) == datet

assert _offset(5).rollforward(dt) == dt
