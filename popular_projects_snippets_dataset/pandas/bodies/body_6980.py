# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_setops.py
first = index[5:20]

union = first.union(first, sort=sort)
# i.e. identity is not preserved when sort is True
assert (union is first) is (not sort)

# This should no longer be the same object, since [] is not consistent,
# both objects will be recast to dtype('O')
union = first.union([], sort=sort)
assert (union is first) is (not sort)

union = Index([]).union(first, sort=sort)
assert (union is first) is (not sort)
