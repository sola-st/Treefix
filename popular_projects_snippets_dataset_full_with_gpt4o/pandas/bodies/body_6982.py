# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_setops.py
first = index[5:20]
first.name = "name"
result = first.difference([], sort)

tm.assert_index_equal(result, first)
