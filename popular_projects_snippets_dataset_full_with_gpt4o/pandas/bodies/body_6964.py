# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_setops.py
# MultiIndex tested separately in tests.indexes.multi.test_setops
index = index_flat

other = index.astype("category")
exact = "equiv" if isinstance(index, RangeIndex) else True

result = getattr(index, method)(other, sort=sort)
expected = getattr(index, method)(index, sort=sort)
tm.assert_index_equal(result, expected, exact=exact)

result = getattr(index, method)(other[:5], sort=sort)
expected = getattr(index, method)(index[:5], sort=sort)
tm.assert_index_equal(result, expected, exact=exact)
