# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_setops.py
# GH#35847
# Test intersections with various name combinations
if not index_flat.is_unique:
    pytest.skip("Randomly generated index_flat was not unique.")
index = index_flat

# Test copy.intersection(copy)
first = index.copy().set_names(fname)
second = index.copy().set_names(sname)
intersect = first.intersection(second)
expected = index.copy().set_names(expected_name)
tm.assert_index_equal(intersect, expected)

# Test copy.intersection(empty)
first = index.copy().set_names(fname)
second = index.drop(index).set_names(sname)
intersect = first.intersection(second)
expected = index.drop(index).set_names(expected_name)
tm.assert_index_equal(intersect, expected)

# Test empty.intersection(copy)
first = index.drop(index).set_names(fname)
second = index.copy().set_names(sname)
intersect = first.intersection(second)
expected = index.drop(index).set_names(expected_name)
tm.assert_index_equal(intersect, expected)

# Test empty.intersection(empty)
first = index.drop(index).set_names(fname)
second = index.drop(index).set_names(sname)
intersect = first.intersection(second)
expected = index.drop(index).set_names(expected_name)
tm.assert_index_equal(intersect, expected)
