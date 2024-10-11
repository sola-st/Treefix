# Extracted from ./data/repos/pandas/pandas/tests/indexes/base_class/test_setops.py
# non-monotonic non-unique
index1 = Index(["A", "B", "A", "C"])
expected = Index(expected_arr, dtype="object")
result = index1.intersection(index2, sort=sort)
if sort is None:
    expected = expected.sort_values()
tm.assert_index_equal(result, expected)
