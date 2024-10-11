# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_setops.py
# Chained unions handles names correctly
i1 = Index([1, 2], name="i1")
i2 = Index([5, 6], name="i2")
i3 = Index([3, 4], name="i3")
union = i1.union(i2.union(i3, sort=sort), sort=sort)
expected = i1.union(i2, sort=sort).union(i3, sort=sort)
tm.assert_index_equal(union, expected)

j1 = Index([1, 2], name="j1")
j2 = Index([], name="j2")
j3 = Index([], name="j3")
union = j1.union(j2.union(j3, sort=sort), sort=sort)
expected = j1.union(j2, sort=sort).union(j3, sort=sort)
tm.assert_index_equal(union, expected)
