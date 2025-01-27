# Extracted from ./data/repos/pandas/pandas/tests/reductions/test_reductions.py
rng = date_range("1/1/2000", "12/31/2000")
rng2 = rng.take(np.random.permutation(len(rng)))

the_min = rng2.min()
the_max = rng2.max()
assert isinstance(the_min, Timestamp)
assert isinstance(the_max, Timestamp)
assert the_min == rng[0]
assert the_max == rng[-1]

assert rng.min() == rng[0]
assert rng.max() == rng[-1]
