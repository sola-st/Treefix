# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge.py
# GH 18885
df1 = DataFrame(
    pd.date_range("2017-10-29 01:00", periods=4, freq="H", tz="Europe/Madrid"),
    columns=["date"],
)
df1["value"] = 1
df2 = DataFrame(
    {
        "date": pd.to_datetime(
            [
                "2017-10-29 03:00:00",
                "2017-10-29 04:00:00",
                "2017-10-29 05:00:00",
            ]
        ),
        "value": 2,
    }
)
df2["date"] = df2["date"].dt.tz_localize("UTC").dt.tz_convert("Europe/Madrid")
result = merge(df1, df2, how="outer", on="date")
expected = DataFrame(
    {
        "date": pd.date_range(
            "2017-10-29 01:00", periods=7, freq="H", tz="Europe/Madrid"
        ),
        "value_x": [1] * 4 + [np.nan] * 3,
        "value_y": [np.nan] * 4 + [2] * 3,
    }
)
tm.assert_frame_equal(result, expected)
