# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_base.py
# casting
arr = np.array(index)
new_index = Index(arr)
tm.assert_contains_all(arr, new_index)
tm.assert_index_equal(index, new_index)
