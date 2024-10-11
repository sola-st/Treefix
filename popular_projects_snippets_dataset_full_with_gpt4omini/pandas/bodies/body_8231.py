# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/methods/test_to_period.py
rng = date_range("01-Jan-2012", periods=8, freq=off)
prng = rng.to_period()
assert prng.freq == "A-DEC"
