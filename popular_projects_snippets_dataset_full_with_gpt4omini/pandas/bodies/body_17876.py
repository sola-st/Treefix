# Extracted from ./data/repos/pandas/pandas/tests/util/test_make_objects.py
# GH#38795 respect 'k' arg
N = np.random.randint(0, 100)
mi = tm.makeMultiIndex(k=N)
assert len(mi) == N
