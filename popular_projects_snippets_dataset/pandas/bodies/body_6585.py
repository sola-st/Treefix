# Extracted from ./data/repos/pandas/pandas/tests/indexes/ranges/test_setops.py
# check that we cast to float, not object
index = RangeIndex(start=0, stop=20, step=2, name="foo")
index = Index(index, dtype=dtype)

flt = index.astype(np.float64)

# bc index.equals(flt), we go through fastpath and get RangeIndex back
result = index.intersection(flt)
tm.assert_index_equal(result, index, exact=True)

result = flt.intersection(index)
tm.assert_index_equal(result, flt, exact=True)

# neither empty, not-equals
result = index.intersection(flt[1:])
tm.assert_index_equal(result, flt[1:], exact=True)

result = flt[1:].intersection(index)
tm.assert_index_equal(result, flt[1:], exact=True)

# empty other
result = index.intersection(flt[:0])
tm.assert_index_equal(result, flt[:0], exact=True)

result = flt[:0].intersection(index)
tm.assert_index_equal(result, flt[:0], exact=True)
