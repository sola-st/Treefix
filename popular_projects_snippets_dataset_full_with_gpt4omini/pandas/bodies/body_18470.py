# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_datetime64.py
# GH#11349
datetime_series = Series([NaT, Timestamp("19900315")])
nat_series_dtype_timestamp = Series([NaT, NaT], dtype="datetime64[ns]")
single_nat_dtype_datetime = Series([NaT], dtype="datetime64[ns]")

# subtraction
tm.assert_series_equal(-NaT + datetime_series, nat_series_dtype_timestamp)
msg = "bad operand type for unary -: 'DatetimeArray'"
with pytest.raises(TypeError, match=msg):
    -single_nat_dtype_datetime + datetime_series

tm.assert_series_equal(
    -NaT + nat_series_dtype_timestamp, nat_series_dtype_timestamp
)
with pytest.raises(TypeError, match=msg):
    -single_nat_dtype_datetime + nat_series_dtype_timestamp

# addition
tm.assert_series_equal(
    nat_series_dtype_timestamp + NaT, nat_series_dtype_timestamp
)
tm.assert_series_equal(
    NaT + nat_series_dtype_timestamp, nat_series_dtype_timestamp
)

tm.assert_series_equal(
    nat_series_dtype_timestamp + NaT, nat_series_dtype_timestamp
)
tm.assert_series_equal(
    NaT + nat_series_dtype_timestamp, nat_series_dtype_timestamp
)
