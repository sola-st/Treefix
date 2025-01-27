# Extracted from ./data/repos/pandas/pandas/tests/indexes/base_class/test_setops.py
first = Index(first_list, name=first_name)
second = Index(second_list, name=second_name)
union = first.union(second, sort=sort)

vals = set(first_list).union(second_list)

if sort is None and len(first_list) > 0 and len(second_list) > 0:
    expected = Index(sorted(vals), name=expected_name)
    tm.assert_index_equal(union, expected)
else:
    expected = Index(vals, name=expected_name)
    tm.equalContents(union, expected)
