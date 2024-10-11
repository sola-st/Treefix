# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_timedelta64.py
# GH 11349
timedelta_series = Series([NaT, Timedelta("1s")])
nat_series_dtype_timedelta = Series([NaT, NaT], dtype="timedelta64[ns]")
single_nat_dtype_timedelta = Series([NaT], dtype="timedelta64[ns]")

# subtraction
tm.assert_series_equal(timedelta_series - NaT, nat_series_dtype_timedelta)
tm.assert_series_equal(-NaT + timedelta_series, nat_series_dtype_timedelta)

tm.assert_series_equal(
    timedelta_series - single_nat_dtype_timedelta, nat_series_dtype_timedelta
)
tm.assert_series_equal(
    -single_nat_dtype_timedelta + timedelta_series, nat_series_dtype_timedelta
)

# addition
tm.assert_series_equal(
    nat_series_dtype_timedelta + NaT, nat_series_dtype_timedelta
)
tm.assert_series_equal(
    NaT + nat_series_dtype_timedelta, nat_series_dtype_timedelta
)

tm.assert_series_equal(
    nat_series_dtype_timedelta + single_nat_dtype_timedelta,
    nat_series_dtype_timedelta,
)
tm.assert_series_equal(
    single_nat_dtype_timedelta + nat_series_dtype_timedelta,
    nat_series_dtype_timedelta,
)

tm.assert_series_equal(timedelta_series + NaT, nat_series_dtype_timedelta)
tm.assert_series_equal(NaT + timedelta_series, nat_series_dtype_timedelta)

tm.assert_series_equal(
    timedelta_series + single_nat_dtype_timedelta, nat_series_dtype_timedelta
)
tm.assert_series_equal(
    single_nat_dtype_timedelta + timedelta_series, nat_series_dtype_timedelta
)

tm.assert_series_equal(
    nat_series_dtype_timedelta + NaT, nat_series_dtype_timedelta
)
tm.assert_series_equal(
    NaT + nat_series_dtype_timedelta, nat_series_dtype_timedelta
)

tm.assert_series_equal(
    nat_series_dtype_timedelta + single_nat_dtype_timedelta,
    nat_series_dtype_timedelta,
)
tm.assert_series_equal(
    single_nat_dtype_timedelta + nat_series_dtype_timedelta,
    nat_series_dtype_timedelta,
)

# multiplication
tm.assert_series_equal(
    nat_series_dtype_timedelta * 1.0, nat_series_dtype_timedelta
)
tm.assert_series_equal(
    1.0 * nat_series_dtype_timedelta, nat_series_dtype_timedelta
)

tm.assert_series_equal(timedelta_series * 1, timedelta_series)
tm.assert_series_equal(1 * timedelta_series, timedelta_series)

tm.assert_series_equal(timedelta_series * 1.5, Series([NaT, Timedelta("1.5s")]))
tm.assert_series_equal(1.5 * timedelta_series, Series([NaT, Timedelta("1.5s")]))

tm.assert_series_equal(timedelta_series * np.nan, nat_series_dtype_timedelta)
tm.assert_series_equal(np.nan * timedelta_series, nat_series_dtype_timedelta)

# division
tm.assert_series_equal(timedelta_series / 2, Series([NaT, Timedelta("0.5s")]))
tm.assert_series_equal(timedelta_series / 2.0, Series([NaT, Timedelta("0.5s")]))
tm.assert_series_equal(timedelta_series / np.nan, nat_series_dtype_timedelta)
