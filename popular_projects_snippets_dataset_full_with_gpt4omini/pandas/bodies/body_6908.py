# Extracted from ./data/repos/pandas/pandas/tests/indexes/base_class/test_setops.py
# (same results for py2 and py3 but sortedness not tested elsewhere)
index = Index([0, "a", 1, "b", 2, "c"])
first = index[:4]
second = index[3:]

result = first.difference(second, sort)
expected = Index([0, "a", 1])
if sort is None:
    expected = Index(safe_sort(expected))
tm.assert_index_equal(result, expected)
