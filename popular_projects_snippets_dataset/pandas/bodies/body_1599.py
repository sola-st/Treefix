# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
dtype = float_numpy_dtype
ser = Series(np.random.rand(10), index=np.arange(10, 20, dtype=dtype))

assert len(ser.loc[12.0:]) == 8
assert len(ser.loc[12.5:]) == 7

idx = np.arange(10, 20, dtype=dtype)
idx[2] = 12.2
ser.index = idx
assert len(ser.loc[12.0:]) == 8
assert len(ser.loc[12.5:]) == 7
