# Extracted from ./data/repos/pandas/pandas/tests/internals/test_internals.py
# dont use np.delete on values, as that will coerce from DTA/TDA to ndarray
arr = np.arange(20, dtype="i8").reshape(5, 4).view("m8[ns]")
df = DataFrame(arr)
blk = df._mgr.blocks[0]
assert isinstance(blk.values, TimedeltaArray)

nb = blk.delete(1)
assert len(nb) == 2
assert isinstance(nb[0].values, TimedeltaArray)
assert isinstance(nb[1].values, TimedeltaArray)

df = DataFrame(arr.view("M8[ns]"))
blk = df._mgr.blocks[0]
assert isinstance(blk.values, DatetimeArray)

nb = blk.delete([1, 3])
assert len(nb) == 2
assert isinstance(nb[0].values, DatetimeArray)
assert isinstance(nb[1].values, DatetimeArray)
