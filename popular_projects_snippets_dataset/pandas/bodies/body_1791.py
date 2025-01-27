# Extracted from ./data/repos/pandas/pandas/tests/resample/test_datetime_index.py
# 5172
dti = DatetimeIndex([datetime(2012, 11, 4, 23)], tz="US/Eastern").as_unit(unit)
df = DataFrame([5], index=dti)

dti = DatetimeIndex(df.index.normalize(), freq="D").as_unit(unit)
expected = DataFrame([5], index=dti)
tm.assert_frame_equal(df.resample(rule="D").sum(), expected)
df.resample(rule="MS").sum()
tm.assert_frame_equal(
    df.resample(rule="MS").sum(),
    DataFrame(
        [5],
        index=DatetimeIndex(
            [datetime(2012, 11, 1)], tz="US/Eastern", freq="MS"
        ).as_unit(unit),
    ),
)

dti = date_range(
    "2013-09-30", "2013-11-02", freq="30Min", tz="Europe/Paris"
).as_unit(unit)
values = range(dti.size)
df = DataFrame({"a": values, "b": values, "c": values}, index=dti, dtype="int64")
how = {"a": "min", "b": "max", "c": "count"}

tm.assert_frame_equal(
    df.resample("W-MON").agg(how)[["a", "b", "c"]],
    DataFrame(
        {
            "a": [0, 48, 384, 720, 1056, 1394],
            "b": [47, 383, 719, 1055, 1393, 1586],
            "c": [48, 336, 336, 336, 338, 193],
        },
        index=date_range(
            "9/30/2013", "11/4/2013", freq="W-MON", tz="Europe/Paris"
        ).as_unit(unit),
    ),
    "W-MON Frequency",
)

tm.assert_frame_equal(
    df.resample("2W-MON").agg(how)[["a", "b", "c"]],
    DataFrame(
        {
            "a": [0, 48, 720, 1394],
            "b": [47, 719, 1393, 1586],
            "c": [48, 672, 674, 193],
        },
        index=date_range(
            "9/30/2013", "11/11/2013", freq="2W-MON", tz="Europe/Paris"
        ).as_unit(unit),
    ),
    "2W-MON Frequency",
)

tm.assert_frame_equal(
    df.resample("MS").agg(how)[["a", "b", "c"]],
    DataFrame(
        {"a": [0, 48, 1538], "b": [47, 1537, 1586], "c": [48, 1490, 49]},
        index=date_range(
            "9/1/2013", "11/1/2013", freq="MS", tz="Europe/Paris"
        ).as_unit(unit),
    ),
    "MS Frequency",
)

tm.assert_frame_equal(
    df.resample("2MS").agg(how)[["a", "b", "c"]],
    DataFrame(
        {"a": [0, 1538], "b": [1537, 1586], "c": [1538, 49]},
        index=date_range(
            "9/1/2013", "11/1/2013", freq="2MS", tz="Europe/Paris"
        ).as_unit(unit),
    ),
    "2MS Frequency",
)

df_daily = df["10/26/2013":"10/29/2013"]
tm.assert_frame_equal(
    df_daily.resample("D").agg({"a": "min", "b": "max", "c": "count"})[
        ["a", "b", "c"]
    ],
    DataFrame(
        {
            "a": [1248, 1296, 1346, 1394],
            "b": [1295, 1345, 1393, 1441],
            "c": [48, 50, 48, 48],
        },
        index=date_range(
            "10/26/2013", "10/29/2013", freq="D", tz="Europe/Paris"
        ).as_unit(unit),
    ),
    "D Frequency",
)
