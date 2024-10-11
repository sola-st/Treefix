# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge.py
left = DataFrame({"a": 0, "b": 1}, index=range(10))
right = DataFrame({"c": "foo", "d": "bar"}, index=range(10))

merged = merge(left, right, left_index=True, right_index=True, copy=False)

assert np.shares_memory(merged["a"]._values, left["a"]._values)
assert np.shares_memory(merged["d"]._values, right["d"]._values)
