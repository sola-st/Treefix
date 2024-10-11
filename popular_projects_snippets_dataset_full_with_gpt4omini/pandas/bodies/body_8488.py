# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_partial_slicing.py
# GH 4294
# partial slice on a series mi
ser = DataFrame(
    np.random.rand(1000, 1000), index=date_range("2000-1-1", periods=1000)
).stack()

s2 = ser[:-1].copy()
expected = s2["2000-1-4"]
result = s2[Timestamp("2000-1-4")]
tm.assert_series_equal(result, expected)

result = ser[Timestamp("2000-1-4")]
expected = ser["2000-1-4"]
tm.assert_series_equal(result, expected)

df2 = DataFrame(ser)
expected = df2.xs("2000-1-4")
result = df2.loc[Timestamp("2000-1-4")]
tm.assert_frame_equal(result, expected)
