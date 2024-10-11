# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_replace.py
ser = pd.Series(datetime_series.index)
tm.assert_series_equal(ser.replace(np.nan, 0), ser.fillna(0))

# malformed
msg = r"Replacement lists must match in length\. Expecting 3 got 2"
with pytest.raises(ValueError, match=msg):
    ser.replace([1, 2, 3], [np.nan, 0])

# ser is dt64 so can't hold 1 or 2, so this replace is a no-op
result = ser.replace([1, 2], [np.nan, 0])
tm.assert_series_equal(result, ser)

ser = pd.Series([0, 1, 2, 3, 4])
result = ser.replace([0, 1, 2, 3, 4], [4, 3, 2, 1, 0])
tm.assert_series_equal(result, pd.Series([4, 3, 2, 1, 0]))
