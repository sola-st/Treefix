# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_partial_slicing.py
# GH#24892 we get Series back regardless of whether our DTI is monotonic
dti = date_range(start="2015-5-13 23:59:00", freq="min", periods=3)
ser = Series(range(3), index=dti)

# non-monotonic index
ser2 = Series(range(3), index=[dti[1], dti[0], dti[2]])

# key with resolution strictly lower than "min"
key = "2015-5-14 00"

# monotonic increasing index
result = ser.loc[key]
expected = ser.iloc[1:]
tm.assert_series_equal(result, expected)

# monotonic decreasing index
result = ser.iloc[::-1].loc[key]
expected = ser.iloc[::-1][:-1]
tm.assert_series_equal(result, expected)

# non-monotonic index
result2 = ser2.loc[key]
expected2 = ser2.iloc[::2]
tm.assert_series_equal(result2, expected2)
