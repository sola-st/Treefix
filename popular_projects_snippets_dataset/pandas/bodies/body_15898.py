# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_unique.py
# GH 46128
dti1 = date_range("2016-01-01", periods=3)
ii1 = IntervalIndex.from_breaks(dti1)
ser1 = Series(ii1)
uni1 = ser1.unique()
tm.assert_interval_array_equal(ser1.array, uni1)

dti2 = date_range("2016-01-01", periods=3, tz="US/Eastern")
ii2 = IntervalIndex.from_breaks(dti2)
ser2 = Series(ii2)
uni2 = ser2.unique()
tm.assert_interval_array_equal(ser2.array, uni2)

assert uni1.dtype != uni2.dtype
