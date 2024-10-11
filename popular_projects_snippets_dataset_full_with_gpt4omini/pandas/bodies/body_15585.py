# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_fillna.py
# DatetimeLikeBlock
ser = Series(
    [
        Timestamp("2011-01-01 10:00"),
        NaT,
        Timestamp("2011-01-03 10:00"),
        NaT,
    ]
)
null_loc = Series([False, True, False, True])

result = ser.fillna(Timestamp("2011-01-02 10:00"))
expected = Series(
    [
        Timestamp("2011-01-01 10:00"),
        Timestamp("2011-01-02 10:00"),
        Timestamp("2011-01-03 10:00"),
        Timestamp("2011-01-02 10:00"),
    ]
)
tm.assert_series_equal(expected, result)
# check s is not changed
tm.assert_series_equal(isna(ser), null_loc)

result = ser.fillna(Timestamp("2011-01-02 10:00", tz=tz))
expected = Series(
    [
        Timestamp("2011-01-01 10:00"),
        Timestamp("2011-01-02 10:00", tz=tz),
        Timestamp("2011-01-03 10:00"),
        Timestamp("2011-01-02 10:00", tz=tz),
    ]
)
tm.assert_series_equal(expected, result)
tm.assert_series_equal(isna(ser), null_loc)

result = ser.fillna("AAA")
expected = Series(
    [
        Timestamp("2011-01-01 10:00"),
        "AAA",
        Timestamp("2011-01-03 10:00"),
        "AAA",
    ],
    dtype=object,
)
tm.assert_series_equal(expected, result)
tm.assert_series_equal(isna(ser), null_loc)

result = ser.fillna(
    {
        1: Timestamp("2011-01-02 10:00", tz=tz),
        3: Timestamp("2011-01-04 10:00"),
    }
)
expected = Series(
    [
        Timestamp("2011-01-01 10:00"),
        Timestamp("2011-01-02 10:00", tz=tz),
        Timestamp("2011-01-03 10:00"),
        Timestamp("2011-01-04 10:00"),
    ]
)
tm.assert_series_equal(expected, result)
tm.assert_series_equal(isna(ser), null_loc)

result = ser.fillna(
    {1: Timestamp("2011-01-02 10:00"), 3: Timestamp("2011-01-04 10:00")}
)
expected = Series(
    [
        Timestamp("2011-01-01 10:00"),
        Timestamp("2011-01-02 10:00"),
        Timestamp("2011-01-03 10:00"),
        Timestamp("2011-01-04 10:00"),
    ]
)
tm.assert_series_equal(expected, result)
tm.assert_series_equal(isna(ser), null_loc)

# DatetimeTZBlock
idx = DatetimeIndex(["2011-01-01 10:00", NaT, "2011-01-03 10:00", NaT], tz=tz)
ser = Series(idx)
assert ser.dtype == f"datetime64[ns, {tz}]"
tm.assert_series_equal(isna(ser), null_loc)

result = ser.fillna(Timestamp("2011-01-02 10:00"))
expected = Series(
    [
        Timestamp("2011-01-01 10:00", tz=tz),
        Timestamp("2011-01-02 10:00"),
        Timestamp("2011-01-03 10:00", tz=tz),
        Timestamp("2011-01-02 10:00"),
    ]
)
tm.assert_series_equal(expected, result)
tm.assert_series_equal(isna(ser), null_loc)

result = ser.fillna(Timestamp("2011-01-02 10:00", tz=tz))
idx = DatetimeIndex(
    [
        "2011-01-01 10:00",
        "2011-01-02 10:00",
        "2011-01-03 10:00",
        "2011-01-02 10:00",
    ],
    tz=tz,
)
expected = Series(idx)
tm.assert_series_equal(expected, result)
tm.assert_series_equal(isna(ser), null_loc)

result = ser.fillna(Timestamp("2011-01-02 10:00", tz=tz).to_pydatetime())
idx = DatetimeIndex(
    [
        "2011-01-01 10:00",
        "2011-01-02 10:00",
        "2011-01-03 10:00",
        "2011-01-02 10:00",
    ],
    tz=tz,
)
expected = Series(idx)
tm.assert_series_equal(expected, result)
tm.assert_series_equal(isna(ser), null_loc)

result = ser.fillna("AAA")
expected = Series(
    [
        Timestamp("2011-01-01 10:00", tz=tz),
        "AAA",
        Timestamp("2011-01-03 10:00", tz=tz),
        "AAA",
    ],
    dtype=object,
)
tm.assert_series_equal(expected, result)
tm.assert_series_equal(isna(ser), null_loc)

result = ser.fillna(
    {
        1: Timestamp("2011-01-02 10:00", tz=tz),
        3: Timestamp("2011-01-04 10:00"),
    }
)
expected = Series(
    [
        Timestamp("2011-01-01 10:00", tz=tz),
        Timestamp("2011-01-02 10:00", tz=tz),
        Timestamp("2011-01-03 10:00", tz=tz),
        Timestamp("2011-01-04 10:00"),
    ]
)
tm.assert_series_equal(expected, result)
tm.assert_series_equal(isna(ser), null_loc)

result = ser.fillna(
    {
        1: Timestamp("2011-01-02 10:00", tz=tz),
        3: Timestamp("2011-01-04 10:00", tz=tz),
    }
)
expected = Series(
    [
        Timestamp("2011-01-01 10:00", tz=tz),
        Timestamp("2011-01-02 10:00", tz=tz),
        Timestamp("2011-01-03 10:00", tz=tz),
        Timestamp("2011-01-04 10:00", tz=tz),
    ]
)
tm.assert_series_equal(expected, result)
tm.assert_series_equal(isna(ser), null_loc)

# filling with a naive/other zone, coerce to object
result = ser.fillna(Timestamp("20130101"))
expected = Series(
    [
        Timestamp("2011-01-01 10:00", tz=tz),
        Timestamp("2013-01-01"),
        Timestamp("2011-01-03 10:00", tz=tz),
        Timestamp("2013-01-01"),
    ]
)
tm.assert_series_equal(expected, result)
tm.assert_series_equal(isna(ser), null_loc)

# pre-2.0 fillna with mixed tzs would cast to object, in 2.0
#  it retains dtype.
result = ser.fillna(Timestamp("20130101", tz="US/Pacific"))
expected = Series(
    [
        Timestamp("2011-01-01 10:00", tz=tz),
        Timestamp("2013-01-01", tz="US/Pacific").tz_convert(tz),
        Timestamp("2011-01-03 10:00", tz=tz),
        Timestamp("2013-01-01", tz="US/Pacific").tz_convert(tz),
    ]
)
tm.assert_series_equal(expected, result)
tm.assert_series_equal(isna(ser), null_loc)
