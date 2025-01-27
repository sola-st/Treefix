# Extracted from ./data/repos/pandas/pandas/tests/scalar/period/test_period.py
freqs = ["A", "M", "Q", "D", "H", "T", "S"]

period = Period(ordinal=-1, freq="D")
for freq in freqs:
    repr(period.asfreq(freq))

for freq in freqs:
    period = Period(ordinal=-1, freq=freq)
    repr(period)
    assert period.year == 1969

period = Period(ordinal=-1, freq="B")
repr(period)
period = Period(ordinal=-1, freq="W")
repr(period)
