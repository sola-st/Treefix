# Extracted from ./data/repos/pandas/pandas/tests/indexes/base_class/test_constructors.py
# GH #45608
result = Index(tuple_list)
expected = MultiIndex.from_tuples(tuple_list)

tm.assert_index_equal(result, expected)
