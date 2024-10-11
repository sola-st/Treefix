# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_combine_first.py
values = tm.makeIntIndex(20).values.astype(float)
series = Series(values, index=tm.makeIntIndex(20))

series_copy = series * 2
series_copy[::2] = np.NaN

# nothing used from the input
combined = series.combine_first(series_copy)

tm.assert_series_equal(combined, series)

# Holes filled from input
combined = series_copy.combine_first(series)
assert np.isfinite(combined).all()

tm.assert_series_equal(combined[::2], series[::2])
tm.assert_series_equal(combined[1::2], series_copy[1::2])

# mixed types
index = tm.makeStringIndex(20)
floats = Series(np.random.randn(20), index=index)
strings = Series(tm.makeStringIndex(10), index=index[::2])

combined = strings.combine_first(floats)

tm.assert_series_equal(strings, combined.loc[index[::2]])
tm.assert_series_equal(floats[1::2].astype(object), combined.loc[index[1::2]])

# corner case
ser = Series([1.0, 2, 3], index=[0, 1, 2])
empty = Series([], index=[], dtype=object)
result = ser.combine_first(empty)
ser.index = ser.index.astype("O")
tm.assert_series_equal(ser, result)
