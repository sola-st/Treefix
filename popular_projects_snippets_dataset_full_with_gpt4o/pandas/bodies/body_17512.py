# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_month.py
shift = klass(
    [
        Timestamp("2000-01-15 00:15:00", tz="US/Central"),
        Timestamp("2000-02-15", tz="US/Central"),
    ],
    name="a",
)

with tm.assert_produces_warning(None):
    # GH#22535 check that we don't get a FutureWarning from adding
    # an integer array to PeriodIndex
    result = shift + SemiMonthEnd()
    result2 = SemiMonthEnd() + shift

exp = klass(
    [
        Timestamp("2000-01-31 00:15:00", tz="US/Central"),
        Timestamp("2000-02-29", tz="US/Central"),
    ],
    name="a",
)
tm.assert_equal(result, exp)
tm.assert_equal(result2, exp)

shift = klass(
    [
        Timestamp("2000-01-01 00:15:00", tz="US/Central"),
        Timestamp("2000-02-01", tz="US/Central"),
    ],
    name="a",
)

with tm.assert_produces_warning(None):
    # GH#22535 check that we don't get a FutureWarning from adding
    # an integer array to PeriodIndex
    result = shift + SemiMonthEnd()
    result2 = SemiMonthEnd() + shift

exp = klass(
    [
        Timestamp("2000-01-15 00:15:00", tz="US/Central"),
        Timestamp("2000-02-15", tz="US/Central"),
    ],
    name="a",
)
tm.assert_equal(result, exp)
tm.assert_equal(result2, exp)
