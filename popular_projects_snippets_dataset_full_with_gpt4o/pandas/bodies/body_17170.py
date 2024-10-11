# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_pivot.py
dates1 = [
    "2011-07-19 07:00:00",
    "2011-07-19 08:00:00",
    "2011-07-19 09:00:00",
    "2011-07-19 07:00:00",
    "2011-07-19 08:00:00",
    "2011-07-19 09:00:00",
]
dates2 = [
    "2013-01-01 15:00:00",
    "2013-01-01 15:00:00",
    "2013-01-01 15:00:00",
    "2013-02-01 15:00:00",
    "2013-02-01 15:00:00",
    "2013-02-01 15:00:00",
]
df = DataFrame(
    {
        "label": ["a", "a", "a", "b", "b", "b"],
        "dt1": dates1,
        "dt2": dates2,
        "value1": np.arange(6, dtype="int64"),
        "value2": [1, 2] * 3,
    }
)
df["dt1"] = df["dt1"].apply(lambda d: pd.Timestamp(d, tz="US/Pacific"))
df["dt2"] = df["dt2"].apply(lambda d: pd.Timestamp(d, tz="Asia/Tokyo"))

exp_idx = pd.DatetimeIndex(
    ["2011-07-19 07:00:00", "2011-07-19 08:00:00", "2011-07-19 09:00:00"],
    tz="US/Pacific",
    name="dt1",
)
exp_col1 = Index(["value1", "value1"])
exp_col2 = Index(["a", "b"], name="label")
exp_col = MultiIndex.from_arrays([exp_col1, exp_col2])
expected = DataFrame([[0, 3], [1, 4], [2, 5]], index=exp_idx, columns=exp_col)
result = pivot_table(df, index=["dt1"], columns=["label"], values=["value1"])
tm.assert_frame_equal(result, expected)

exp_col1 = Index(["sum", "sum", "sum", "sum", "mean", "mean", "mean", "mean"])
exp_col2 = Index(["value1", "value1", "value2", "value2"] * 2)
exp_col3 = pd.DatetimeIndex(
    ["2013-01-01 15:00:00", "2013-02-01 15:00:00"] * 4,
    tz="Asia/Tokyo",
    name="dt2",
)
exp_col = MultiIndex.from_arrays([exp_col1, exp_col2, exp_col3])
expected = DataFrame(
    np.array(
        [
            [0, 3, 1, 2, 0, 3, 1, 2],
            [1, 4, 2, 1, 1, 4, 2, 1],
            [2, 5, 1, 2, 2, 5, 1, 2],
        ],
        dtype="int64",
    ),
    index=exp_idx,
    columns=exp_col,
)

result = pivot_table(
    df,
    index=["dt1"],
    columns=["dt2"],
    values=["value1", "value2"],
    aggfunc=[np.sum, np.mean],
)
tm.assert_frame_equal(result, expected)
