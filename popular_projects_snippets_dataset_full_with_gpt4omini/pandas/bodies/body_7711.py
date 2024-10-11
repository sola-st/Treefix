# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_equivalence.py
assert idx.equals(idx)
assert idx.equals(idx.copy())
assert idx.equals(idx.astype(object))
assert idx.equals(idx.to_flat_index())
assert idx.equals(idx.to_flat_index().astype("category"))

assert not idx.equals(list(idx))
assert not idx.equals(np.array(idx))

same_values = Index(idx, dtype=object)
assert idx.equals(same_values)
assert same_values.equals(idx)

if idx.nlevels == 1:
    # do not test MultiIndex
    assert not idx.equals(Series(idx))
