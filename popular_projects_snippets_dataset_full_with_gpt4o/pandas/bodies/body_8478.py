# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_partial_slicing.py
# GH#31064
dti = date_range("2019-12-31 23:59:55.999999999", periods=10, freq="s")

ser = Series(range(10), index=dti)
result = ser[partial_dtime]
expected = ser.iloc[:5]
tm.assert_series_equal(result, expected)
