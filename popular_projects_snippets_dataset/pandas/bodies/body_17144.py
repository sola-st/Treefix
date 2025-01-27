# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_pivot.py
df = DataFrame(
    {
        "p1": [
            pd.Period("2013-01-01", "D"),
            pd.Period("2013-01-02", "D"),
            pd.Period("2013-01-01", "D"),
            pd.Period("2013-01-02", "D"),
        ],
        "p2": [
            pd.Period("2013-01", "M"),
            pd.Period("2013-01", "M"),
            pd.Period("2013-02", "M"),
            pd.Period("2013-02", "M"),
        ],
        "data1": np.arange(4, dtype="int64"),
        "data2": np.arange(4, dtype="int64"),
    }
)

exp_col1 = Index(["data1", "data1", "data2", "data2"])
exp_col2 = pd.PeriodIndex(["2013-01", "2013-02"] * 2, name="p2", freq="M")
exp_col = MultiIndex.from_arrays([exp_col1, exp_col2])
expected = DataFrame(
    [[0, 2, 0, 2], [1, 3, 1, 3]],
    index=pd.PeriodIndex(["2013-01-01", "2013-01-02"], name="p1", freq="D"),
    columns=exp_col,
)
if method:
    pv = df.pivot(index="p1", columns="p2")
else:
    pv = pd.pivot(df, index="p1", columns="p2")
tm.assert_frame_equal(pv, expected)

expected = DataFrame(
    [[0, 2], [1, 3]],
    index=pd.PeriodIndex(["2013-01-01", "2013-01-02"], name="p1", freq="D"),
    columns=pd.PeriodIndex(["2013-01", "2013-02"], name="p2", freq="M"),
)
if method:
    pv = df.pivot(index="p1", columns="p2", values="data1")
else:
    pv = pd.pivot(df, index="p1", columns="p2", values="data1")
tm.assert_frame_equal(pv, expected)
