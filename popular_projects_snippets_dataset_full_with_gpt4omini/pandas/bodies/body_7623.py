# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_indexing.py
# GH#19132
idx = MultiIndex.from_arrays([[1, np.nan, 2]])
assert np.nan in idx

idx = MultiIndex.from_arrays([[1, 2], [np.nan, 3]])
assert np.nan not in idx
assert (1, np.nan) in idx
