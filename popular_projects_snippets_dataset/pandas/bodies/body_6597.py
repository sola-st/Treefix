# Extracted from ./data/repos/pandas/pandas/tests/indexes/ranges/test_setops.py
# case with intersection of length 1 but RangeIndex is not preserved
idx = Index(range(10))

other = idx[3:4]
result = idx.difference(other)
expected = Index([0, 1, 2, 4, 5, 6, 7, 8, 9])
tm.assert_index_equal(result, expected, exact=True)

# case with other.step / self.step > 2
other = idx[::3]
result = idx.difference(other)
expected = Index([1, 2, 4, 5, 7, 8])
tm.assert_index_equal(result, expected, exact=True)

# cases with only reaching one end of left
obj = Index(range(20))
other = obj[:10:2]
result = obj.difference(other)
expected = Index([1, 3, 5, 7, 9] + list(range(10, 20)))
tm.assert_index_equal(result, expected, exact=True)

other = obj[1:11:2]
result = obj.difference(other)
expected = Index([0, 2, 4, 6, 8, 10] + list(range(11, 20)))
tm.assert_index_equal(result, expected, exact=True)
