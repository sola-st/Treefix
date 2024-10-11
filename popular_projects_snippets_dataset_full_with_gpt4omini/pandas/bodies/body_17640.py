# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_custom_business_month.py
dt = datetime(2012, 10, 23)

result = dt + CBMonthBegin(10)
assert result == datetime(2013, 8, 1)

result = dt + CDay(100) - CDay(100)
assert result == dt

off = CBMonthBegin() * 6
rs = datetime(2012, 1, 1) - off
xp = datetime(2011, 7, 1)
assert rs == xp

st = datetime(2011, 12, 18)
rs = st + off

xp = datetime(2012, 6, 1)
assert rs == xp
