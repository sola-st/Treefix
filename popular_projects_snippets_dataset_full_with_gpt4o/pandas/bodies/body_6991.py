# Extracted from ./data/repos/pandas/pandas/tests/indexes/categorical/test_append.py
# append cats with the same categories
result = ci[:3].append(ci[3:])
tm.assert_index_equal(result, ci, exact=True)

foos = [ci[:1], ci[1:3], ci[3:]]
result = foos[0].append(foos[1:])
tm.assert_index_equal(result, ci, exact=True)
