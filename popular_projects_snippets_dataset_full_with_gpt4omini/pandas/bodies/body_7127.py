# Extracted from ./data/repos/pandas/pandas/tests/indexes/common.py
# GH32898, GH36840
idx = simple_index
idx.get_loc(idx[0])  # populates the _cache.
copy = idx.copy()

assert copy._cache is idx._cache
