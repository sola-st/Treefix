# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/test_period.py
pi = period_range(freq="A", start="1/1/2001", end="12/1/2009")
assert len(pi) == 9

pi = period_range(freq="Q", start="1/1/2001", end="12/1/2009")
assert len(pi) == 4 * 9

pi = period_range(freq="M", start="1/1/2001", end="12/1/2009")
assert len(pi) == 12 * 9

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

msg = "start and end must have same freq"
with pytest.raises(ValueError, match=msg):
    period_range(start=start, end=end_intv)

end_intv = Period("2005-05-01", "B")
i1 = period_range(start=start, end=end_intv)

msg = (
    "Of the three parameters: start, end, and periods, exactly two "
    "must be specified"
)
with pytest.raises(ValueError, match=msg):
    period_range(start=start)

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
with pytest.raises(ValueError, match=msg):
    PeriodIndex(vals)
