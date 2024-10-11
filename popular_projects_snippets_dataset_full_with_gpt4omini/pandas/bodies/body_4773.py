# Extracted from ./data/repos/pandas/pandas/tests/strings/test_strings.py
ser = Series(
    ["ABC", "ＡＢＣ", "１２３", np.nan, "ｱｲｴ"],
    index=["a", "b", "c", "d", "e"],
    dtype=any_string_dtype,
)
expected = Series(expected, index=["a", "b", "c", "d", "e"], dtype=any_string_dtype)
result = ser.str.normalize(form)
tm.assert_series_equal(result, expected)
