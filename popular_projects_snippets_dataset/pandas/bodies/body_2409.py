# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_indexing.py
# Difficulties with mixed-type data
# Created as float type
dm = DataFrame(index=range(3), columns=range(3))

coercable_series = Series([Decimal(1) for _ in range(3)], index=range(3))
uncoercable_series = Series(["foo", "bzr", "baz"], index=range(3))

dm[0] = np.ones(3)
assert len(dm.columns) == 3

dm[1] = coercable_series
assert len(dm.columns) == 3

dm[2] = uncoercable_series
assert len(dm.columns) == 3
assert dm[2].dtype == np.object_
