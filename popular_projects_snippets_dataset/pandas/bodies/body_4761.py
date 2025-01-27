# Extracted from ./data/repos/pandas/pandas/tests/strings/test_strings.py
ser = Series(
    ["short", "a bit longer", "evenlongerthanthat", "", np.nan],
    dtype=any_string_dtype,
)
expected = Series(expected, dtype=any_string_dtype)
result = ser.str.slice_replace(start, stop, repl)
tm.assert_series_equal(result, expected)
