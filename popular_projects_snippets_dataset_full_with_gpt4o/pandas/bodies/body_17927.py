# Extracted from ./data/repos/pandas/pandas/tests/util/test_shares_memory.py
obj = pd.interval_range(1, 5)

assert tm.shares_memory(obj, obj)
assert tm.shares_memory(obj, obj._data)
assert tm.shares_memory(obj, obj[::-1])
assert tm.shares_memory(obj, obj[:2])

assert not tm.shares_memory(obj, obj._data.copy())
