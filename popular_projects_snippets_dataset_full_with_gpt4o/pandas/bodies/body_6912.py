# Extracted from ./data/repos/pandas/pandas/tests/indexes/base_class/test_setops.py
# GH 13432
idx1 = Index([0, 1, "A", "B"])
idx2 = Index([0, 2, "A", "C"])
result = getattr(idx1, diff_type)(idx2)
expected = Index(expected)
tm.assert_index_equal(result, expected)
