# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_dropna.py
ser = Series(
    [np.nan, 1, 2, 3],
    IntervalIndex.from_arrays([np.nan, 0, 1, 2], [np.nan, 1, 2, 3]),
)

result = ser.dropna()
expected = ser.iloc[1:]
tm.assert_series_equal(result, expected)
