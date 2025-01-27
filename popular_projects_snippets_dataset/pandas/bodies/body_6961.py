# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_setops.py
# GH#20040
# If taking difference of a set and itself, it
# needs to preserve the type of the index
if not index.is_unique:
    exit()
result = index.difference(index, sort=sort)
expected = index[:0]
tm.assert_index_equal(result, expected, exact=True)
