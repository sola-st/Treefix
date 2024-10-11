# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_setitem.py
# GH#24096 altering a datetime64tz Series inplace invalidates the
#  `freq` attribute on the underlying DatetimeIndex

dti = date_range("20130101", periods=3, tz="US/Eastern")
ts = dti[1]
ser = Series(dti)
assert ser._values is not dti
assert ser._values._ndarray.base is not dti._data._ndarray.base
assert dti.freq == "D"
ser.iloc[1] = NaT
assert ser._values.freq is None

# check that the DatetimeIndex was not altered in place
assert ser._values is not dti
assert ser._values._ndarray.base is not dti._data._ndarray.base
assert dti[1] == ts
assert dti.freq == "D"
