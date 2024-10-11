# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_datetime64.py
# GH#10699
s = date_range("2000-01-01", "2000-01-31", name="a")
s = tm.box_expected(s, box_with_array)
result = s + DateOffset(years=1)
result2 = DateOffset(years=1) + s
exp = date_range("2001-01-01", "2001-01-31", name="a")._with_freq(None)
exp = tm.box_expected(exp, box_with_array)
tm.assert_equal(result, exp)
tm.assert_equal(result2, exp)

result = s - DateOffset(years=1)
exp = date_range("1999-01-01", "1999-01-31", name="a")._with_freq(None)
exp = tm.box_expected(exp, box_with_array)
tm.assert_equal(result, exp)

s = DatetimeIndex(
    [
        Timestamp("2000-01-15 00:15:00", tz="US/Central"),
        Timestamp("2000-02-15", tz="US/Central"),
    ],
    name="a",
)
s = tm.box_expected(s, box_with_array)
result = s + pd.offsets.Day()
result2 = pd.offsets.Day() + s
exp = DatetimeIndex(
    [
        Timestamp("2000-01-16 00:15:00", tz="US/Central"),
        Timestamp("2000-02-16", tz="US/Central"),
    ],
    name="a",
)
exp = tm.box_expected(exp, box_with_array)
tm.assert_equal(result, exp)
tm.assert_equal(result2, exp)

s = DatetimeIndex(
    [
        Timestamp("2000-01-15 00:15:00", tz="US/Central"),
        Timestamp("2000-02-15", tz="US/Central"),
    ],
    name="a",
)
s = tm.box_expected(s, box_with_array)
result = s + pd.offsets.MonthEnd()
result2 = pd.offsets.MonthEnd() + s
exp = DatetimeIndex(
    [
        Timestamp("2000-01-31 00:15:00", tz="US/Central"),
        Timestamp("2000-02-29", tz="US/Central"),
    ],
    name="a",
)
exp = tm.box_expected(exp, box_with_array)
tm.assert_equal(result, exp)
tm.assert_equal(result2, exp)
