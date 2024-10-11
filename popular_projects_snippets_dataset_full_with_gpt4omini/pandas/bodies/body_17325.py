# Extracted from ./data/repos/pandas/pandas/tests/generic/test_generic.py
indices = [1, 5, -2, 6, 3, -1]
out = ser.take(indices)
expected = Series(
    data=ser.values.take(indices),
    index=ser.index.take(indices),
    dtype=ser.dtype,
)
tm.assert_series_equal(out, expected)
