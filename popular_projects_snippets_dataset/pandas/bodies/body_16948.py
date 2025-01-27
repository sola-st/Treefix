# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_datetimes.py
# GH 12396

first = DataFrame(Series([pd.NaT, pd.NaT]).dt.tz_localize(tz1))
second = DataFrame(Series([pd.NaT]).dt.tz_localize(tz2), columns=[1])
expected = DataFrame(
    {
        0: Series([pd.NaT, pd.NaT]).dt.tz_localize(tz1),
        1: Series([pd.NaT, pd.NaT]).dt.tz_localize(tz2),
    }
)
result = concat([first, second], axis=1)
tm.assert_frame_equal(result, expected)
