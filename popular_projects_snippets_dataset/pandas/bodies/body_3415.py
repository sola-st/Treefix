# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_values.py

# interleave with object
result = timezone_frame.assign(D="foo").values
expected = np.array(
    [
        [
            Timestamp("2013-01-01 00:00:00"),
            Timestamp("2013-01-02 00:00:00"),
            Timestamp("2013-01-03 00:00:00"),
        ],
        [
            Timestamp("2013-01-01 00:00:00-0500", tz="US/Eastern"),
            NaT,
            Timestamp("2013-01-03 00:00:00-0500", tz="US/Eastern"),
        ],
        [
            Timestamp("2013-01-01 00:00:00+0100", tz="CET"),
            NaT,
            Timestamp("2013-01-03 00:00:00+0100", tz="CET"),
        ],
        ["foo", "foo", "foo"],
    ],
    dtype=object,
).T
tm.assert_numpy_array_equal(result, expected)

# interleave with only datetime64[ns]
result = timezone_frame.values
expected = np.array(
    [
        [
            Timestamp("2013-01-01 00:00:00"),
            Timestamp("2013-01-02 00:00:00"),
            Timestamp("2013-01-03 00:00:00"),
        ],
        [
            Timestamp("2013-01-01 00:00:00-0500", tz="US/Eastern"),
            NaT,
            Timestamp("2013-01-03 00:00:00-0500", tz="US/Eastern"),
        ],
        [
            Timestamp("2013-01-01 00:00:00+0100", tz="CET"),
            NaT,
            Timestamp("2013-01-03 00:00:00+0100", tz="CET"),
        ],
    ],
    dtype=object,
).T
tm.assert_numpy_array_equal(result, expected)
