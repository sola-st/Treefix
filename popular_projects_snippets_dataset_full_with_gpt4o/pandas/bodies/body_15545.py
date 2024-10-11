# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_infer_objects.py
# GH#50096
# case where we don't need to do inference because it is already non-object
obj = index_or_series(np.array([1, 2, 3], dtype="int64"))

result = obj.infer_objects(copy=False)
assert tm.shares_memory(result, obj)

# case where we try to do inference but can't do better than object
obj2 = index_or_series(np.array(["foo", 2], dtype=object))
result2 = obj2.infer_objects(copy=False)
assert tm.shares_memory(result2, obj2)
