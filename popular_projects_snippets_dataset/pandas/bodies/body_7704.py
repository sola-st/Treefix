# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_constructors.py
# check that inference behavior matches the base class

v = date.today()

arr = [v, v]

idx = Index(arr)
assert idx.dtype == object

mi = MultiIndex.from_arrays([arr])
lev = mi.levels[0]
assert lev.dtype == object

mi = MultiIndex.from_product([arr])
lev = mi.levels[0]
assert lev.dtype == object

mi = MultiIndex.from_tuples([(x,) for x in arr])
lev = mi.levels[0]
assert lev.dtype == object
