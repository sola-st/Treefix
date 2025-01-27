# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_base.py
# GH 12766

# Test that returning a single tuple from an Index
#   returns an Index.
index = tm.makeIntIndex(3)
result = tm.makeIntIndex(3).map(lambda x: (x,))
expected = Index([(i,) for i in index])
tm.assert_index_equal(result, expected)

# Test that returning a tuple from a map of a single index
#   returns a MultiIndex object.
result = index.map(lambda x: (x, x == 1))
expected = MultiIndex.from_tuples([(i, i == 1) for i in index])
tm.assert_index_equal(result, expected)
