# Extracted from ./data/repos/pandas/pandas/tests/indexes/base_class/test_reshape.py

# GH 7256
# validate neg/pos inserts
result = Index(["b", "c", "d"])

# test 0th element
tm.assert_index_equal(Index(["a", "b", "c", "d"]), result.insert(0, "a"))

# test Nth element that follows Python list behavior
tm.assert_index_equal(Index(["b", "c", "e", "d"]), result.insert(-1, "e"))

# test loc +/- neq (0, -1)
tm.assert_index_equal(result.insert(1, "z"), result.insert(-2, "z"))

# test empty
null_index = Index([])
tm.assert_index_equal(Index(["a"]), null_index.insert(0, "a"))
