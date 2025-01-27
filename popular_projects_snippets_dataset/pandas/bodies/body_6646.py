# Extracted from ./data/repos/pandas/pandas/tests/indexes/ranges/test_range.py
index = simple_index
index.name = "foo"

# scalar indexing
res = index[1]
expected = 2
assert res == expected

res = index[-1]
expected = 18
assert res == expected

# slicing
# slice value completion
index_slice = index[:]
expected = index
tm.assert_index_equal(index_slice, expected)

# positive slice values
index_slice = index[7:10:2]
expected = Index([14, 18], name="foo")
tm.assert_index_equal(index_slice, expected, exact="equiv")

# negative slice values
index_slice = index[-1:-5:-2]
expected = Index([18, 14], name="foo")
tm.assert_index_equal(index_slice, expected, exact="equiv")

# stop overshoot
index_slice = index[2:100:4]
expected = Index([4, 12], name="foo")
tm.assert_index_equal(index_slice, expected, exact="equiv")

# reverse
index_slice = index[::-1]
expected = Index(index.values[::-1], name="foo")
tm.assert_index_equal(index_slice, expected, exact="equiv")

index_slice = index[-8::-1]
expected = Index([4, 2, 0], name="foo")
tm.assert_index_equal(index_slice, expected, exact="equiv")

index_slice = index[-40::-1]
expected = Index(np.array([], dtype=np.int64), name="foo")
tm.assert_index_equal(index_slice, expected, exact="equiv")

index_slice = index[40::-1]
expected = Index(index.values[40::-1], name="foo")
tm.assert_index_equal(index_slice, expected, exact="equiv")

index_slice = index[10::-1]
expected = Index(index.values[::-1], name="foo")
tm.assert_index_equal(index_slice, expected, exact="equiv")
