# Extracted from ./data/repos/pandas/pandas/tests/indexes/ranges/test_setops.py
# GH#44085 ensure we respect the sort keyword

idx = Index(range(4))[::-1]
other = Index(range(3, 4))

result = idx.difference(other)
expected = Index(range(3))
tm.assert_index_equal(result, expected, exact=True)

result = idx.difference(other, sort=False)
expected = expected[::-1]
tm.assert_index_equal(result, expected, exact=True)

# case where the intersection is empty
other = range(10, 12)
result = idx.difference(other, sort=None)
expected = idx[::-1]
tm.assert_index_equal(result, expected, exact=True)
