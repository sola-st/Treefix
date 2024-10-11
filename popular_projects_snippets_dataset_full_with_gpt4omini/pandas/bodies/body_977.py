# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_floats.py

# same as above, but for floats
index = Index(np.arange(5.0)) + 0.1
s = gen_obj(frame_or_series, index)

expected = s.iloc[3:4]

# getitem
result = indexer_sl(s)[idx]
assert isinstance(result, type(s))
tm.assert_equal(result, expected)

# setitem
s2 = s.copy()
indexer_sl(s2)[idx] = 0
result = indexer_sl(s2)[idx].values.ravel()
assert (result == 0).all()
