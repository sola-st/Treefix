# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_setops.py
if isinstance(index, MultiIndex):
    names = [[x] * index.nlevels for x in names]
index = index.rename(names[0])
other = index.rename(names[1])

assert index.equals(other)

result = index.difference(other)
expected = index[:0].rename(names[2])
tm.assert_index_equal(result, expected)
