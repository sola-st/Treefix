# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
# GH#39882
ser = Series(
    datetimelikes,
    dtype="object",
)
result_series = to_datetime(ser, errors="coerce")
expected_series = Series(
    expected_values,
    dtype="datetime64[ns]",
)
tm.assert_series_equal(result_series, expected_series)
