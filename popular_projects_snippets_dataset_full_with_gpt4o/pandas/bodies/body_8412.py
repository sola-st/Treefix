# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_date_range.py
# GH 10885
result_1 = date_range("2005-01-12 10:00", "2005-01-12 16:00", freq="345min")
result_2 = date_range("2005-01-13 10:00", "2005-01-13 16:00", freq="345min")
expected_1 = DatetimeIndex(
    ["2005-01-12 10:00:00", "2005-01-12 15:45:00"],
    dtype="datetime64[ns]",
    freq="345T",
    tz=None,
)
expected_2 = DatetimeIndex(
    ["2005-01-13 10:00:00", "2005-01-13 15:45:00"],
    dtype="datetime64[ns]",
    freq="345T",
    tz=None,
)
tm.assert_index_equal(result_1, expected_1)
tm.assert_index_equal(result_2, expected_2)
