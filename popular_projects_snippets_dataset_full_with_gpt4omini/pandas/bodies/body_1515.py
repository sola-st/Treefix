# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# GH20722
# Test whether loc accept uint64 max value as index.
umax = np.iinfo("uint64").max
ser = Series([1, 2], index=[umax - 1, umax])

result = ser.loc[umax - 1]
expected = ser.iloc[0]
assert result == expected

result = ser.loc[[umax - 1]]
expected = ser.iloc[[0]]
tm.assert_series_equal(result, expected)

result = ser.loc[[umax - 1, umax]]
tm.assert_series_equal(result, ser)
