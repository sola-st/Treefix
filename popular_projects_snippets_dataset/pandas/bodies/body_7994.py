# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_index_new.py
# GH#49594 match Series behavior on ndarray[object] of all bools
arr = np.array([True, False], dtype=object)
res = Index(arr)
assert res.dtype == object

# since the point is matching Series behavior, let's double check
assert Series(arr).dtype == object
