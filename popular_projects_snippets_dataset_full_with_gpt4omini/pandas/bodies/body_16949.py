# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_datetimes.py
# GH 12396

# tz-naive
first = Series([pd.NaT, pd.NaT]).dt.tz_localize(tz1)
second = DataFrame(
    [
        [Timestamp("2015/01/01", tz=tz2)],
        [Timestamp("2016/01/01", tz=tz2)],
    ],
    index=[2, 3],
)

expected = DataFrame(
    [
        pd.NaT,
        pd.NaT,
        Timestamp("2015/01/01", tz=tz2),
        Timestamp("2016/01/01", tz=tz2),
    ]
)
if tz1 != tz2:
    expected = expected.astype(object)

result = concat([first, second])
tm.assert_frame_equal(result, expected)
