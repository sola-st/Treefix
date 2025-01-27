# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_transpose.py
dti = date_range("2016-01-01", periods=6, tz="US/Pacific")
arr = dti._data.reshape(3, 2)
df = DataFrame(arr)
assert df._mgr.nblocks == 1

result = df.T
assert result._mgr.nblocks == 1

rtrip = result._mgr.blocks[0].values
assert np.shares_memory(arr._ndarray, rtrip._ndarray)
