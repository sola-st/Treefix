# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/test_constructors.py
pi = period_range(freq="A", start="1/1/2001", end="12/1/2009")
assert len(pi) == 9

pi = period_range(freq="Q", start="1/1/2001", end="12/1/2009")
assert len(pi) == 4 * 9

pi = period_range(freq="M", start="1/1/2001", end="12/1/2009")
assert len(pi) == 12 * 9

pi = period_range(freq="D", start="1/1/2001", end="12/31/2009")
assert len(pi) == 365 * 9 + 2

pi = period_range(freq="B", start="1/1/2001", end="12/31/2009")
assert len(pi) == 261 * 9

pi = period_range(freq="H", start="1/1/2001", end="12/31/2001 23:00")
assert len(pi) == 365 * 24

pi = period_range(freq="Min", start="1/1/2001", end="1/1/2001 23:59")
assert len(pi) == 24 * 60

pi = period_range(freq="S", start="1/1/2001", end="1/1/2001 23:59:59")
assert len(pi) == 24 * 60 * 60

start = Period("02-Apr-2005", "B")
i1 = period_range(start=start, periods=20)
assert len(i1) == 20
assert i1.freq == start.freq
assert i1[0] == start

end_intv = Period("2006-12-31", "W")
i1 = period_range(end=end_intv, periods=10)
assert len(i1) == 10
assert i1.freq == end_intv.freq
assert i1[-1] == end_intv

end_intv = Period("2006-12-31", "1w")
i2 = period_range(end=end_intv, periods=10)
assert len(i1) == len(i2)
assert (i1 == i2).all()
assert i1.freq == i2.freq

end_intv = Period("2005-05-01", "B")
i1 = period_range(start=start, end=end_intv)

# infer freq from first element
i2 = PeriodIndex([end_intv, Period("2005-05-05", "B")])
assert len(i2) == 2
assert i2[0] == end_intv

i2 = PeriodIndex(np.array([end_intv, Period("2005-05-05", "B")]))
assert len(i2) == 2
assert i2[0] == end_intv

# Mixed freq should fail
vals = [end_intv, Period("2006-12-31", "w")]
msg = r"Input has different freq=W-SUN from PeriodIndex\(freq=B\)"
with pytest.raises(IncompatibleFrequency, match=msg):
    PeriodIndex(vals)
vals = np.array(vals)
with pytest.raises(IncompatibleFrequency, match=msg):
    PeriodIndex(vals)

# tuple freq disallowed GH#34703
with pytest.raises(TypeError, match="pass as a string instead"):
    Period("2006-12-31", ("w", 1))
