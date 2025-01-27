# Extracted from ./data/repos/pandas/pandas/tests/indexes/base_class/test_setops.py
index = Index([0, "a", 1, "b", 2, "c"])
first = index[3:]
second = index[:5]

result = first.union(second)

expected = Index([0, 1, 2, "a", "b", "c"])
tm.assert_index_equal(result, expected)
