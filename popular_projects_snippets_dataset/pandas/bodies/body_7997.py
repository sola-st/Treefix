# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_index_new.py
# GH#18505 : valid tuples containing NaN
values = [(1, "two"), (3.0, na_value)]
result = Index(vtype(values))
expected = MultiIndex.from_tuples(values)
tm.assert_index_equal(result, expected)
