# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_interpolate.py
ser = Series([10, 11, 12, 13])

expected = Series(
    [11.00, 11.25, 11.50, 11.75, 12.00, 12.25, 12.50, 12.75, 13.00],
    index=Index([1.0, 1.25, 1.5, 1.75, 2.0, 2.25, 2.5, 2.75, 3.0]),
)
# interpolate at new_index
new_index = ser.index.union(Index([1.25, 1.5, 1.75, 2.25, 2.5, 2.75])).astype(
    float
)
interp_s = ser.reindex(new_index).interpolate(method="from_derivatives")
tm.assert_series_equal(interp_s[1:3], expected)
