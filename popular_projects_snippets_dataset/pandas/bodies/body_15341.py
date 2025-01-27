# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_getitem.py
# GH#36210
dti = date_range("2016-01-01", periods=4, tz="US/Pacific")
key = np.array([True, True, False, False])

ser = Series(dti._data)

res = ser[key]
assert res._values._ndarray.base is None

# compare with numeric case for reference
ser2 = Series(range(4))
res2 = ser2[key]
assert res2._values.base is None
