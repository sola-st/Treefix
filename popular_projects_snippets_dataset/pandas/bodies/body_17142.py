# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_pivot.py
# GH 5878
df = DataFrame(
    {
        "dt1": [
            datetime(2013, 1, 1, 9, 0),
            datetime(2013, 1, 2, 9, 0),
            datetime(2013, 1, 1, 9, 0),
            datetime(2013, 1, 2, 9, 0),
        ],
        "dt2": [
            datetime(2014, 1, 1, 9, 0),
            datetime(2014, 1, 1, 9, 0),
            datetime(2014, 1, 2, 9, 0),
            datetime(2014, 1, 2, 9, 0),
        ],
        "data1": np.arange(4, dtype="int64"),
        "data2": np.arange(4, dtype="int64"),
    }
)

df["dt1"] = df["dt1"].apply(lambda d: pd.Timestamp(d, tz="US/Pacific"))
df["dt2"] = df["dt2"].apply(lambda d: pd.Timestamp(d, tz="Asia/Tokyo"))

exp_col1 = Index(["data1", "data1", "data2", "data2"])
exp_col2 = pd.DatetimeIndex(
    ["2014/01/01 09:00", "2014/01/02 09:00"] * 2, name="dt2", tz="Asia/Tokyo"
)
exp_col = MultiIndex.from_arrays([exp_col1, exp_col2])
expected = DataFrame(
    [[0, 2, 0, 2], [1, 3, 1, 3]],
    index=pd.DatetimeIndex(
        ["2013/01/01 09:00", "2013/01/02 09:00"], name="dt1", tz="US/Pacific"
    ),
    columns=exp_col,
)

if method:
    pv = df.pivot(index="dt1", columns="dt2")
else:
    pv = pd.pivot(df, index="dt1", columns="dt2")
tm.assert_frame_equal(pv, expected)

expected = DataFrame(
    [[0, 2], [1, 3]],
    index=pd.DatetimeIndex(
        ["2013/01/01 09:00", "2013/01/02 09:00"], name="dt1", tz="US/Pacific"
    ),
    columns=pd.DatetimeIndex(
        ["2014/01/01 09:00", "2014/01/02 09:00"], name="dt2", tz="Asia/Tokyo"
    ),
)

if method:
    pv = df.pivot(index="dt1", columns="dt2", values="data1")
else:
    pv = pd.pivot(df, index="dt1", columns="dt2", values="data1")
tm.assert_frame_equal(pv, expected)
