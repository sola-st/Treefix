# Extracted from ./data/repos/pandas/pandas/tests/scalar/period/test_period.py
left, right = Period("2011", freq="A"), Period("2007", freq="A")
result = left - right
assert result == 4 * right.freq

msg = r"Input has different freq=M from Period\(freq=A-DEC\)"
with pytest.raises(IncompatibleFrequency, match=msg):
    left - Period("2007-01", freq="M")
