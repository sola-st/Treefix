# Extracted from ./data/repos/pandas/pandas/tests/scalar/period/test_period.py
jan = Period("2000-01", "M")
day = Period("2012-01-01", "D")

assert not jan == day
assert jan != day
msg = r"Input has different freq=D from Period\(freq=M\)"
with pytest.raises(IncompatibleFrequency, match=msg):
    jan < day
with pytest.raises(IncompatibleFrequency, match=msg):
    jan <= day
with pytest.raises(IncompatibleFrequency, match=msg):
    jan > day
with pytest.raises(IncompatibleFrequency, match=msg):
    jan >= day
