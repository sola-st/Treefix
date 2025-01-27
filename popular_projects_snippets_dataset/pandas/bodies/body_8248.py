# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/methods/test_shift.py
rng = date_range(START, END, freq=freq)
shifted = rng.shift(5)
assert shifted[0] == rng[5]
assert shifted.freq == rng.freq

shifted = rng.shift(-5)
assert shifted[5] == rng[0]
assert shifted.freq == rng.freq

shifted = rng.shift(0)
assert shifted[0] == rng[0]
assert shifted.freq == rng.freq
