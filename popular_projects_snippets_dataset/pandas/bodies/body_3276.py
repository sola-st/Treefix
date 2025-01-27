# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_astype.py
# astype
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
expected = DataFrame(
    expected,
    index=timezone_frame.index,
    columns=timezone_frame.columns,
    dtype=object,
)
result = timezone_frame.astype(object)
tm.assert_frame_equal(result, expected)

msg = "Cannot use .astype to convert from timezone-aware dtype to timezone-"
with pytest.raises(TypeError, match=msg):
    # dt64tz->dt64 deprecated
    timezone_frame.astype("datetime64[ns]")
