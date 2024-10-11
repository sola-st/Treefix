# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_setops.py
# GH#9943, GH#9862
# Test unions with various name combinations
# Do not test MultiIndex or repeats
if not index_flat.is_unique:
    pytest.skip("Randomly generated index_flat was not unique.")
index = index_flat

# Test copy.union(copy)
first = index.copy().set_names(fname)
second = index.copy().set_names(sname)
union = first.union(second)
expected = index.copy().set_names(expected_name)
tm.assert_index_equal(union, expected)

# Test copy.union(empty)
first = index.copy().set_names(fname)
second = index.drop(index).set_names(sname)
union = first.union(second)
expected = index.copy().set_names(expected_name)
tm.assert_index_equal(union, expected)

# Test empty.union(copy)
first = index.drop(index).set_names(fname)
second = index.copy().set_names(sname)
union = first.union(second)
expected = index.copy().set_names(expected_name)
tm.assert_index_equal(union, expected)

# Test empty.union(empty)
first = index.drop(index).set_names(fname)
second = index.drop(index).set_names(sname)
union = first.union(second)
expected = index.drop(index).set_names(expected_name)
tm.assert_index_equal(union, expected)
