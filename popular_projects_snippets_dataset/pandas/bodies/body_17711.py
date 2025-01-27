# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_business_day.py
dt = datetime(2012, 10, 23)

result = dt + _offset(10)
assert result == datetime(2012, 11, 6)

result = dt + _offset(100) - _offset(100)
assert result == dt

off = _offset() * 6
rs = datetime(2012, 1, 1) - off
xp = datetime(2011, 12, 23)
assert rs == xp

st = datetime(2011, 12, 18)
rs = st + off
xp = datetime(2011, 12, 26)
assert rs == xp

off = _offset() * 10
rs = datetime(2014, 1, 5) + off  # see #5890
xp = datetime(2014, 1, 17)
assert rs == xp
