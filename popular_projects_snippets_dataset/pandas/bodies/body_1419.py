# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_indexing.py

# GH 11836
# if we have an index type and set it with something that looks
# to numpy like the same, but is actually, not
# (e.g. setting with a float or string '0')
# then we need to coerce to object

# integer indexes
for s in [Series(range(5)), Series(range(5), index=range(1, 6))]:

    assert is_integer_dtype(s.index)

    s2 = s.copy()
    indexer(s2)[0.1] = 0
    assert is_float_dtype(s2.index)
    assert indexer(s2)[0.1] == 0

    s2 = s.copy()
    indexer(s2)[0.0] = 0
    exp = s.index
    if 0 not in s:
        exp = Index(s.index.tolist() + [0])
    tm.assert_index_equal(s2.index, exp)

    s2 = s.copy()
    indexer(s2)["0"] = 0
    assert s2.index.is_object()

for s in [Series(range(5), index=np.arange(5.0))]:

    assert is_float_dtype(s.index)

    s2 = s.copy()
    indexer(s2)[0.1] = 0
    assert is_float_dtype(s2.index)
    assert indexer(s2)[0.1] == 0

    s2 = s.copy()
    indexer(s2)[0.0] = 0
    tm.assert_index_equal(s2.index, s.index)

    s2 = s.copy()
    indexer(s2)["0"] = 0
    assert s2.index.is_object()
