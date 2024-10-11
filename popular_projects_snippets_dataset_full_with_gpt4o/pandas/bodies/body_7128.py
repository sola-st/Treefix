# Extracted from ./data/repos/pandas/pandas/tests/indexes/common.py
# GH32669, GH36840
idx = simple_index
idx.get_loc(idx[0])  # populates the _cache.
shallow_copy = idx._view()

assert shallow_copy._cache is idx._cache

shallow_copy = idx._shallow_copy(idx._data)
assert shallow_copy._cache is not idx._cache
assert shallow_copy._cache == {}
