# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_constructors.py
rng = date_range("1/1/2000", "1/2/2000", freq="5min")

rng2 = DatetimeIndex(rng)
assert rng.freq == rng2.freq
