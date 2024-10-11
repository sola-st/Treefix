# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
# coerce we can process
expected = DatetimeIndex(
    [Timestamp("1970-01-02"), Timestamp("1970-01-03")] + ["NaT"] * 1
)
result = to_datetime([1, 2, bad_val], unit="D", errors="coerce")
tm.assert_index_equal(result, expected)
