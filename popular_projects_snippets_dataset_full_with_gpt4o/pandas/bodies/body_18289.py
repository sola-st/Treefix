# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_object.py
# note this test is _not_ aimed at timedelta64-dtyped Series
# as of 2.0 we retain object dtype when ser.dtype == object
ser = Series(
    [pd.Timedelta("1 days"), pd.Timedelta("2 days"), pd.Timedelta("3 days")],
    dtype=dtype,
)
expected = Series(
    [pd.Timedelta("4 days"), pd.Timedelta("5 days"), pd.Timedelta("6 days")],
    dtype=dtype,
)

result = pd.Timedelta("3 days") + ser
tm.assert_series_equal(result, expected)

result = ser + pd.Timedelta("3 days")
tm.assert_series_equal(result, expected)
