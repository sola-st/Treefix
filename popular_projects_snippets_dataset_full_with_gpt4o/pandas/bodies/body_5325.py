# Extracted from ./data/repos/pandas/pandas/tests/scalar/period/test_period.py
p = Period("2011-04-01", freq="D")
result = p + offsets.Day()
exp = Period("2011-04-02", freq="D")
assert result == exp

result = p - offsets.Day(2)
exp = Period("2011-03-30", freq="D")
assert result == exp

msg = r"Input cannot be converted to Period\(freq=D\)"
with pytest.raises(IncompatibleFrequency, match=msg):
    p + offsets.Hour(2)

with pytest.raises(IncompatibleFrequency, match=msg):
    p - offsets.Hour(2)
