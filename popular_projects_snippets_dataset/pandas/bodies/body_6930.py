# Extracted from ./data/repos/pandas/pandas/tests/indexes/base_class/test_indexing.py
# Go through the libindex path for which using
# _bin_search vs ndarray.searchsorted makes a difference

lev = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
dti = pd.date_range("2016-01-01", periods=100)

mi = pd.MultiIndex.from_product([lev, range(10**3), dti])
oidx = mi.to_flat_index()

loc = len(oidx) // 2
tup = oidx[loc]

res = oidx.get_loc(tup)
assert res == loc
