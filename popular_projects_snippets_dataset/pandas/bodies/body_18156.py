# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_period.py
other = mismatched_freq
rng = period_range("2014", "2024", freq="A")
msg = "Input has different freq(=.+)? from Period.*?\\(freq=A-DEC\\)"
with pytest.raises(IncompatibleFrequency, match=msg):
    rng + other
with pytest.raises(IncompatibleFrequency, match=msg):
    rng += other
with pytest.raises(IncompatibleFrequency, match=msg):
    rng - other
with pytest.raises(IncompatibleFrequency, match=msg):
    rng -= other
