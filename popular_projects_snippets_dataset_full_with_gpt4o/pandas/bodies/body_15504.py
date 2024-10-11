# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_round.py
ser = Series(
    [1.123, 2.123, 3.123],
    index=range(3),
    dtype=any_float_dtype,
)
result = round(ser)
expected_rounded0 = Series(
    [1.0, 2.0, 3.0], index=range(3), dtype=any_float_dtype
)
tm.assert_series_equal(result, expected_rounded0)

decimals = 2
expected_rounded = Series(
    [1.12, 2.12, 3.12], index=range(3), dtype=any_float_dtype
)
result = round(ser, decimals)
tm.assert_series_equal(result, expected_rounded)
