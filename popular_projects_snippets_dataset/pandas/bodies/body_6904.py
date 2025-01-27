# Extracted from ./data/repos/pandas/pandas/tests/indexes/base_class/test_setops.py
result = Index(["c", "b", "a"]).intersection(["b", "a"])
expected = Index(["b", "a"])
tm.assert_index_equal(result, expected)
