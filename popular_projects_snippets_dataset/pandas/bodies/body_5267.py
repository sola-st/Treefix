# Extracted from ./data/repos/pandas/pandas/tests/scalar/period/test_period.py
p1 = Period("2011-01", freq="3M")
p2 = Period("2011-01", freq="M")
assert p1.ordinal == p2.ordinal

assert p1.freq == offsets.MonthEnd(3)
assert p1.freqstr == "3M"

assert p2.freq == offsets.MonthEnd()
assert p2.freqstr == "M"

result = p1 + 1
assert result.ordinal == (p2 + 3).ordinal

assert result.freq == p1.freq
assert result.freqstr == "3M"

result = p1 - 1
assert result.ordinal == (p2 - 3).ordinal
assert result.freq == p1.freq
assert result.freqstr == "3M"

msg = "Frequency must be positive, because it represents span: -3M"
with pytest.raises(ValueError, match=msg):
    Period("2011-01", freq="-3M")

msg = "Frequency must be positive, because it represents span: 0M"
with pytest.raises(ValueError, match=msg):
    Period("2011-01", freq="0M")
