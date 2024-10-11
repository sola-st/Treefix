# Extracted from ./data/repos/pandas/pandas/tests/indexes/base_class/test_setops.py
# (same results for py2 and py3 but sortedness not tested elsewhere)
index = Index([0, "a", 1, "b", 2, "c"])
first = index[:5]
second = index[:3]

expected = Index([0, 1, "a"]) if sort is None else Index([0, "a", 1])
result = first.intersection(second, sort=sort)
tm.assert_index_equal(result, expected)
