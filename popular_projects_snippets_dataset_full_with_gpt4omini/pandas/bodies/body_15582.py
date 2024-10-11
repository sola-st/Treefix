# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_fillna.py
# GH#3371
ser = Series(
    [
        Timestamp("20130101"),
        Timestamp("20130101"),
        Timestamp("20130102"),
        Timestamp("20130103 9:01:01"),
    ]
)
td = ser.diff()
obj = frame_or_series(td)

# reg fillna
result = obj.fillna(Timedelta(seconds=0))
expected = Series(
    [
        timedelta(0),
        timedelta(0),
        timedelta(1),
        timedelta(days=1, seconds=9 * 3600 + 60 + 1),
    ]
)
expected = frame_or_series(expected)
tm.assert_equal(result, expected)

# GH#45746 pre-1.? ints were interpreted as seconds.  then that was
#  deprecated and changed to raise. In 2.0 it casts to common dtype,
#  consistent with every other dtype's behavior
res = obj.fillna(1)
expected = obj.astype(object).fillna(1)
tm.assert_equal(res, expected)

result = obj.fillna(Timedelta(seconds=1))
expected = Series(
    [
        timedelta(seconds=1),
        timedelta(0),
        timedelta(1),
        timedelta(days=1, seconds=9 * 3600 + 60 + 1),
    ]
)
expected = frame_or_series(expected)
tm.assert_equal(result, expected)

result = obj.fillna(timedelta(days=1, seconds=1))
expected = Series(
    [
        timedelta(days=1, seconds=1),
        timedelta(0),
        timedelta(1),
        timedelta(days=1, seconds=9 * 3600 + 60 + 1),
    ]
)
expected = frame_or_series(expected)
tm.assert_equal(result, expected)

result = obj.fillna(np.timedelta64(10**9))
expected = Series(
    [
        timedelta(seconds=1),
        timedelta(0),
        timedelta(1),
        timedelta(days=1, seconds=9 * 3600 + 60 + 1),
    ]
)
expected = frame_or_series(expected)
tm.assert_equal(result, expected)

result = obj.fillna(NaT)
expected = Series(
    [
        NaT,
        timedelta(0),
        timedelta(1),
        timedelta(days=1, seconds=9 * 3600 + 60 + 1),
    ],
    dtype="m8[ns]",
)
expected = frame_or_series(expected)
tm.assert_equal(result, expected)

# ffill
td[2] = np.nan
obj = frame_or_series(td)
result = obj.ffill()
expected = td.fillna(Timedelta(seconds=0))
expected[0] = np.nan
expected = frame_or_series(expected)

tm.assert_equal(result, expected)

# bfill
td[2] = np.nan
obj = frame_or_series(td)
result = obj.bfill()
expected = td.fillna(Timedelta(seconds=0))
expected[2] = timedelta(days=1, seconds=9 * 3600 + 60 + 1)
expected = frame_or_series(expected)
tm.assert_equal(result, expected)
