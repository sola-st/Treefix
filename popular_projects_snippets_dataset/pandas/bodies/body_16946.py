# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_datetimes.py
# GH 12396

first = DataFrame([[pd.NaT], [pd.NaT]])
first = first.apply(lambda x: x.dt.tz_localize(tz))
second = DataFrame(
    [[Timestamp("2015/01/01", tz=tz)], [Timestamp("2016/01/01", tz=tz)]],
    index=[2, 3],
)
expected = DataFrame(
    [
        pd.NaT,
        pd.NaT,
        Timestamp("2015/01/01", tz=tz),
        Timestamp("2016/01/01", tz=tz),
    ]
)

result = concat([first, second], axis=0)
tm.assert_frame_equal(result, expected)
