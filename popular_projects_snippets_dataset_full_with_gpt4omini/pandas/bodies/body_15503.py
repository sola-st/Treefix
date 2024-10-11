# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_round.py
# See GH#14197
ser = Series([1.53, np.nan, 0.06], dtype=any_float_dtype)
with tm.assert_produces_warning(None):
    result = ser.round()
expected = Series([2.0, np.nan, 0.0], dtype=any_float_dtype)
tm.assert_series_equal(result, expected)
