# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_datetimes.py
# GH 18523
idx1 = date_range("2011-01-01", periods=3, freq="H", tz="Europe/Paris")
idx2 = date_range(start=idx1[0], end=idx1[-1], freq="H")
df1 = DataFrame({"a": [1, 2, 3]}, index=idx1)
df2 = DataFrame({"b": [1, 2, 3]}, index=idx2)
result = concat([df1, df2], axis=1)

exp_idx = (
    DatetimeIndex(
        [
            "2011-01-01 00:00:00+01:00",
            "2011-01-01 01:00:00+01:00",
            "2011-01-01 02:00:00+01:00",
        ],
        freq="H",
    )
    .tz_convert("UTC")
    .tz_convert("Europe/Paris")
)

expected = DataFrame(
    [[1, 1], [2, 2], [3, 3]], index=exp_idx, columns=["a", "b"]
)

tm.assert_frame_equal(result, expected)

idx3 = date_range("2011-01-01", periods=3, freq="H", tz="Asia/Tokyo")
df3 = DataFrame({"b": [1, 2, 3]}, index=idx3)
result = concat([df1, df3], axis=1)

exp_idx = DatetimeIndex(
    [
        "2010-12-31 15:00:00+00:00",
        "2010-12-31 16:00:00+00:00",
        "2010-12-31 17:00:00+00:00",
        "2010-12-31 23:00:00+00:00",
        "2011-01-01 00:00:00+00:00",
        "2011-01-01 01:00:00+00:00",
    ]
)

expected = DataFrame(
    [
        [np.nan, 1],
        [np.nan, 2],
        [np.nan, 3],
        [1, np.nan],
        [2, np.nan],
        [3, np.nan],
    ],
    index=exp_idx,
    columns=["a", "b"],
)

tm.assert_frame_equal(result, expected)

# GH 13783: Concat after resample
result = concat([df1.resample("H").mean(), df2.resample("H").mean()], sort=True)
expected = DataFrame(
    {"a": [1, 2, 3] + [np.nan] * 3, "b": [np.nan] * 3 + [1, 2, 3]},
    index=idx1.append(idx1),
)
tm.assert_frame_equal(result, expected)
