# Extracted from ./data/repos/pandas/pandas/tests/apply/test_frame_apply.py
other_axis = 1 if axis in {0, "index"} else 0
name1, name2 = float_frame.axes[other_axis].unique()[:2].sort_values()

# all reducers
expected = pd.concat(
    [
        float_frame.mean(axis=axis),
        float_frame.max(axis=axis),
        float_frame.sum(axis=axis),
    ],
    axis=1,
)
expected.columns = ["mean", "max", "sum"]
expected = expected.T if axis in {0, "index"} else expected

result = float_frame.agg(["mean", "max", "sum"], axis=axis)
tm.assert_frame_equal(result, expected)

# dict input with scalars
func = {name1: "mean", name2: "sum"}
result = float_frame.agg(func, axis=axis)
expected = Series(
    [
        float_frame.loc(other_axis)[name1].mean(),
        float_frame.loc(other_axis)[name2].sum(),
    ],
    index=[name1, name2],
)
tm.assert_series_equal(result, expected)

# dict input with lists
func = {name1: ["mean"], name2: ["sum"]}
result = float_frame.agg(func, axis=axis)
expected = DataFrame(
    {
        name1: Series([float_frame.loc(other_axis)[name1].mean()], index=["mean"]),
        name2: Series([float_frame.loc(other_axis)[name2].sum()], index=["sum"]),
    }
)
expected = expected.T if axis in {1, "columns"} else expected
tm.assert_frame_equal(result, expected)

# dict input with lists with multiple
func = {name1: ["mean", "sum"], name2: ["sum", "max"]}
result = float_frame.agg(func, axis=axis)
expected = pd.concat(
    {
        name1: Series(
            [
                float_frame.loc(other_axis)[name1].mean(),
                float_frame.loc(other_axis)[name1].sum(),
            ],
            index=["mean", "sum"],
        ),
        name2: Series(
            [
                float_frame.loc(other_axis)[name2].sum(),
                float_frame.loc(other_axis)[name2].max(),
            ],
            index=["sum", "max"],
        ),
    },
    axis=1,
)
expected = expected.T if axis in {1, "columns"} else expected
tm.assert_frame_equal(result, expected)
