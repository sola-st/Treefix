# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_indexing.py
rng = bdate_range(START, END, freq=freq)
smaller = rng[:5]
exp = DatetimeIndex(rng.view(np.ndarray)[:5], freq=freq)
tm.assert_index_equal(smaller, exp)
assert smaller.freq == exp.freq
assert smaller.freq == rng.freq

sliced = rng[::5]
assert sliced.freq == to_offset(freq) * 5

fancy_indexed = rng[[4, 3, 2, 1, 0]]
assert len(fancy_indexed) == 5
assert isinstance(fancy_indexed, DatetimeIndex)
assert fancy_indexed.freq is None

# 32-bit vs. 64-bit platforms
assert rng[4] == rng[np.int_(4)]
