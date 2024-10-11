# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_setitem.py
# GH#21907, GH#24096
dti = date_range("2016-01-01", periods=10, tz="US/Pacific")
ts = dti[0]
ser = Series(dti)
assert ser._values is not dti
assert ser._values._ndarray.base is not dti._data._ndarray.base
assert ser._mgr.arrays[0] is not dti
assert ser._mgr.arrays[0]._ndarray.base is not dti._data._ndarray.base

ser[::3] = NaT
assert ser[0] is NaT
assert dti[0] == ts
