# Extracted from ./data/repos/pandas/pandas/tests/indexes/common.py
# GH#43921 inserting an element that we know we can hold should
#  not change dtype or type (except for RangeIndex)
index = simple_index

result = index.insert(0, index[0])

expected = Index([index[0]] + list(index), dtype=index.dtype)
tm.assert_index_equal(result, expected, exact=True)
