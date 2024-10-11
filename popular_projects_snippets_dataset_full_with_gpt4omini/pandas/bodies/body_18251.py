# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_numeric.py
# validate that we are handling the RangeIndex overrides to numeric ops
# and returning RangeIndex where possible

idx = RangeIndex(0, 10, 2)

result = idx * 2
expected = RangeIndex(0, 20, 4)
tm.assert_index_equal(result, expected, exact=True)

result = idx + 2
expected = RangeIndex(2, 12, 2)
tm.assert_index_equal(result, expected, exact=True)

result = idx - 2
expected = RangeIndex(-2, 8, 2)
tm.assert_index_equal(result, expected, exact=True)

result = idx / 2
expected = RangeIndex(0, 5, 1).astype("float64")
tm.assert_index_equal(result, expected, exact=True)

result = idx / 4
expected = RangeIndex(0, 10, 2) / 4
tm.assert_index_equal(result, expected, exact=True)

result = idx // 1
expected = idx
tm.assert_index_equal(result, expected, exact=True)

# __mul__
result = idx * idx
expected = Index(idx.values * idx.values)
tm.assert_index_equal(result, expected, exact=True)

# __pow__
idx = RangeIndex(0, 1000, 2)
result = idx**2
expected = Index(idx._values) ** 2
tm.assert_index_equal(Index(result.values), expected, exact=True)
