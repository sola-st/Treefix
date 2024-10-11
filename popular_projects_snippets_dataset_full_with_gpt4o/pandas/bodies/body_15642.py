# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_interpolate.py

ser = Series([10, 11, 12, 13])

# interpolate at new_index where `der` is zero
expected = Series(
    [11.00, 11.25, 11.50, 11.75, 12.00, 12.25, 12.50, 12.75, 13.00],
    index=Index([1.0, 1.25, 1.5, 1.75, 2.0, 2.25, 2.5, 2.75, 3.0]),
)
new_index = ser.index.union(Index([1.25, 1.5, 1.75, 2.25, 2.5, 2.75])).astype(
    float
)
interp_s = ser.reindex(new_index).interpolate(method="akima")
tm.assert_series_equal(interp_s[1:3], expected)

# interpolate at new_index where `der` is a non-zero int
expected = Series(
    [11.0, 1.0, 1.0, 1.0, 12.0, 1.0, 1.0, 1.0, 13.0],
    index=Index([1.0, 1.25, 1.5, 1.75, 2.0, 2.25, 2.5, 2.75, 3.0]),
)
new_index = ser.index.union(Index([1.25, 1.5, 1.75, 2.25, 2.5, 2.75])).astype(
    float
)
interp_s = ser.reindex(new_index).interpolate(method="akima", der=1)
tm.assert_series_equal(interp_s[1:3], expected)
