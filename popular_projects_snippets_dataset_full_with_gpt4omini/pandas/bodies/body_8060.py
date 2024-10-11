# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_base.py
# Test that returning a single object from a MultiIndex
#   returns an Index.
first_level = ["foo", "bar", "baz"]
multi_index = MultiIndex.from_tuples(zip(first_level, [1, 2, 3]))
reduced_index = multi_index.map(lambda x: x[0])
tm.assert_index_equal(reduced_index, Index(first_level))
