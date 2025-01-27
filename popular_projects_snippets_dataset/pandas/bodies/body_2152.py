# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
result = to_datetime([1, 2, "NaT", NaT, np.nan], unit="D")
expected = DatetimeIndex(
    [Timestamp("1970-01-02"), Timestamp("1970-01-03")] + ["NaT"] * 3
)
tm.assert_index_equal(result, expected)
