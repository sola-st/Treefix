# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_base.py
ind = Index(range(10))
assert ind.is_(ind)
assert ind.is_(ind.view().view().view().view())
assert not ind.is_(Index(range(10)))
assert not ind.is_(ind.copy())
assert not ind.is_(ind.copy(deep=False))
assert not ind.is_(ind[:])
assert not ind.is_(np.array(range(10)))

# quasi-implementation dependent
assert ind.is_(ind.view())
ind2 = ind.view()
ind2.name = "bob"
assert ind.is_(ind2)
assert ind2.is_(ind)
# doesn't matter if Indices are *actually* views of underlying data,
assert not ind.is_(Index(ind.values))
arr = np.array(range(1, 11))
ind1 = Index(arr, copy=False)
ind2 = Index(arr, copy=False)
assert not ind1.is_(ind2)
