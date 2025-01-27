# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_pivot.py
# GH 14380
idx = pd.DatetimeIndex(
    ["2011-01-01", "2011-02-01", "2011-01-02", "2011-01-01", "2011-01-02"]
)
df = DataFrame({"A": [1, 2, 3, 4, 5]}, index=idx)
res = df.pivot_table(index=df.index.month, columns=df.index.day)

exp_columns = MultiIndex.from_tuples([("A", 1), ("A", 2)])
exp_columns = exp_columns.set_levels(
    exp_columns.levels[1].astype(np.int32), level=1
)
exp = DataFrame(
    [[2.5, 4.0], [2.0, np.nan]],
    index=Index([1, 2], dtype=np.int32),
    columns=exp_columns,
)
tm.assert_frame_equal(res, exp)

df = DataFrame(
    {
        "A": [1, 2, 3, 4, 5],
        "dt": date_range("2011-01-01", freq="D", periods=5),
    },
    index=idx,
)
res = df.pivot_table(index=df.index.month, columns=Grouper(key="dt", freq="M"))
exp_columns = MultiIndex.from_tuples([("A", pd.Timestamp("2011-01-31"))])
exp_columns.names = [None, "dt"]
exp = DataFrame(
    [3.25, 2.0], index=Index([1, 2], dtype=np.int32), columns=exp_columns
)
tm.assert_frame_equal(res, exp)

res = df.pivot_table(
    index=Grouper(freq="A"), columns=Grouper(key="dt", freq="M")
)
exp = DataFrame(
    [3], index=pd.DatetimeIndex(["2011-12-31"], freq="A"), columns=exp_columns
)
tm.assert_frame_equal(res, exp)
