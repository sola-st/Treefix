# Extracted from ./data/repos/pandas/pandas/tests/indexes/categorical/test_append.py
# empty
result = ci.append([])
tm.assert_index_equal(result, ci, exact=True)
