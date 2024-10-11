# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_getitem.py
rng = date_range("1/1/2000", "3/1/2000", freq="B")

mask = np.zeros(len(rng), dtype=bool)
mask[10:20] = True

masked = rng[mask]
expected = rng[10:20]
assert expected.freq == rng.freq
tm.assert_index_equal(masked, expected)

mask[22] = True
masked = rng[mask]
assert masked.freq is None
