# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
result = Series(to_datetime([0, 1, 2], unit="D", origin="unix"))
expected = Series(
    [Timestamp("1970-01-01"), Timestamp("1970-01-02"), Timestamp("1970-01-03")]
)
tm.assert_series_equal(result, expected)
