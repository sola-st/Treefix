# Extracted from ./data/repos/pandas/pandas/tests/indexes/base_class/test_indexing.py
# case that goes through _maybe_get_bool_indexer
idx = Index(["foo", np.nan, None, "foo", 1.0, None], dtype=object)

# we dont raise KeyError on nan
res = idx.get_loc(np.nan)
assert res == 1

# we only match on None, not on np.nan
res = idx.get_loc(None)
expected = np.array([False, False, True, False, False, True])
tm.assert_numpy_array_equal(res, expected)

# we don't match at all on mismatched NA
with pytest.raises(KeyError, match="NaT"):
    idx.get_loc(NaT)
