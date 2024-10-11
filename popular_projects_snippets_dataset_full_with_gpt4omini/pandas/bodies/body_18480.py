# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_datetime64.py
# GH#11349
timedelta_series = Series([NaT, Timedelta("1s")])
datetime_series = Series([NaT, Timestamp("19900315")])
nat_series_dtype_timedelta = Series([NaT, NaT], dtype="timedelta64[ns]")
nat_series_dtype_timestamp = Series([NaT, NaT], dtype="datetime64[ns]")
single_nat_dtype_datetime = Series([NaT], dtype="datetime64[ns]")
single_nat_dtype_timedelta = Series([NaT], dtype="timedelta64[ns]")

# subtraction
tm.assert_series_equal(
    datetime_series - single_nat_dtype_datetime, nat_series_dtype_timedelta
)

tm.assert_series_equal(
    datetime_series - single_nat_dtype_timedelta, nat_series_dtype_timestamp
)
tm.assert_series_equal(
    -single_nat_dtype_timedelta + datetime_series, nat_series_dtype_timestamp
)

# without a Series wrapping the NaT, it is ambiguous
# whether it is a datetime64 or timedelta64
# defaults to interpreting it as timedelta64
tm.assert_series_equal(
    nat_series_dtype_timestamp - single_nat_dtype_datetime,
    nat_series_dtype_timedelta,
)

tm.assert_series_equal(
    nat_series_dtype_timestamp - single_nat_dtype_timedelta,
    nat_series_dtype_timestamp,
)
tm.assert_series_equal(
    -single_nat_dtype_timedelta + nat_series_dtype_timestamp,
    nat_series_dtype_timestamp,
)
msg = "cannot subtract a datelike"
with pytest.raises(TypeError, match=msg):
    timedelta_series - single_nat_dtype_datetime

# addition
tm.assert_series_equal(
    nat_series_dtype_timestamp + single_nat_dtype_timedelta,
    nat_series_dtype_timestamp,
)
tm.assert_series_equal(
    single_nat_dtype_timedelta + nat_series_dtype_timestamp,
    nat_series_dtype_timestamp,
)

tm.assert_series_equal(
    nat_series_dtype_timestamp + single_nat_dtype_timedelta,
    nat_series_dtype_timestamp,
)
tm.assert_series_equal(
    single_nat_dtype_timedelta + nat_series_dtype_timestamp,
    nat_series_dtype_timestamp,
)

tm.assert_series_equal(
    nat_series_dtype_timedelta + single_nat_dtype_datetime,
    nat_series_dtype_timestamp,
)
tm.assert_series_equal(
    single_nat_dtype_datetime + nat_series_dtype_timedelta,
    nat_series_dtype_timestamp,
)
