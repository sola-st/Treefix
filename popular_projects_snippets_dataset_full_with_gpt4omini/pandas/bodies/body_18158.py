# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_period.py
other = mismatched_freq
rng = period_range("2014-01", "2016-12", freq="M")
msg = "Input has different freq(=.+)? from Period.*?\\(freq=M\\)"
with pytest.raises(IncompatibleFrequency, match=msg):
    rng + other
with pytest.raises(IncompatibleFrequency, match=msg):
    rng += other
with pytest.raises(IncompatibleFrequency, match=msg):
    rng - other
with pytest.raises(IncompatibleFrequency, match=msg):
    rng -= other
