# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_pivot.py
# GH 8103
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
df["dt1"] = df["dt1"].apply(lambda d: pd.Timestamp(d))
df["dt2"] = df["dt2"].apply(lambda d: pd.Timestamp(d))

result = pivot_table(
    df, index="label", columns=df["dt1"].dt.hour, values="value1"
)

exp_idx = Index(["a", "b"], name="label")
expected = DataFrame(
    {7: [0, 3], 8: [1, 4], 9: [2, 5]},
    index=exp_idx,
    columns=Index([7, 8, 9], dtype=np.int32, name="dt1"),
)
tm.assert_frame_equal(result, expected)

result = pivot_table(
    df, index=df["dt2"].dt.month, columns=df["dt1"].dt.hour, values="value1"
)

expected = DataFrame(
    {7: [0, 3], 8: [1, 4], 9: [2, 5]},
    index=Index([1, 2], dtype=np.int32, name="dt2"),
    columns=Index([7, 8, 9], dtype=np.int32, name="dt1"),
)
tm.assert_frame_equal(result, expected)

result = pivot_table(
    df,
    index=df["dt2"].dt.year.values,
    columns=[df["dt1"].dt.hour, df["dt2"].dt.month],
    values="value1",
)

exp_col = MultiIndex.from_arrays(
    [
        np.array([7, 7, 8, 8, 9, 9], dtype=np.int32),
        np.array([1, 2] * 3, dtype=np.int32),
    ],
    names=["dt1", "dt2"],
)
expected = DataFrame(
    np.array([[0, 3, 1, 4, 2, 5]], dtype="int64"),
    index=Index([2013], dtype=np.int32),
    columns=exp_col,
)
tm.assert_frame_equal(result, expected)

result = pivot_table(
    df,
    index=np.array(["X", "X", "X", "X", "Y", "Y"]),
    columns=[df["dt1"].dt.hour, df["dt2"].dt.month],
    values="value1",
)
expected = DataFrame(
    np.array(
        [[0, 3, 1, np.nan, 2, np.nan], [np.nan, np.nan, np.nan, 4, np.nan, 5]]
    ),
    index=["X", "Y"],
    columns=exp_col,
)
tm.assert_frame_equal(result, expected)
