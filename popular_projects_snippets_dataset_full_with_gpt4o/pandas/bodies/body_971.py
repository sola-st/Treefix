# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_floats.py

# scalar float indexers work on a float index
index = Index(np.arange(5.0))
s = gen_obj(frame_or_series, index)

# assert all operations except for iloc are ok
indexer = index[3]
for idxr in [tm.loc, tm.setitem]:
    getitem = idxr is not tm.loc

    # getting
    result = idxr(s)[indexer]
    self.check(result, s, 3, getitem)

    # setting
    s2 = s.copy()

    result = idxr(s2)[indexer]
    self.check(result, s, 3, getitem)

    # random float is a KeyError
    with pytest.raises(KeyError, match=r"^3\.5$"):
        idxr(s)[3.5]

        # contains
assert 3.0 in s

# iloc succeeds with an integer
expected = s.iloc[3]
s2 = s.copy()

s2.iloc[3] = expected
result = s2.iloc[3]
self.check(result, s, 3, False)
