# Extracted from ./data/repos/pandas/pandas/tests/resample/test_resample_api.py
# test with all three Resampler apis and TimeGrouper

np.random.seed(1234)
index = date_range(datetime(2005, 1, 1), datetime(2005, 1, 10), freq="D")
index.name = "date"
df = DataFrame(np.random.rand(10, 2), columns=list("AB"), index=index)
df_col = df.reset_index()
df_mult = df_col.copy()
df_mult.index = pd.MultiIndex.from_arrays(
    [range(10), df.index], names=["index", "date"]
)
r = df.resample("2D")
cases = [
    r,
    df_col.resample("2D", on="date"),
    df_mult.resample("2D", level="date"),
    df.groupby(pd.Grouper(freq="2D")),
]

a_mean = r["A"].mean()
a_std = r["A"].std()
a_sum = r["A"].sum()
b_mean = r["B"].mean()
b_std = r["B"].std()
b_sum = r["B"].sum()

expected = pd.concat([a_mean, a_std, b_mean, b_std], axis=1)
expected.columns = pd.MultiIndex.from_product([["A", "B"], ["mean", "std"]])
for t in cases:
    # In case 2, "date" is an index and a column, so agg still tries to agg
    if t == cases[2]:
        # .var on dt64 column raises
        msg = "Cannot cast DatetimeArray to dtype float64"
        with pytest.raises(TypeError, match=msg):
            t.aggregate([np.mean, np.std])
    else:
        result = t.aggregate([np.mean, np.std])
        tm.assert_frame_equal(result, expected)

expected = pd.concat([a_mean, b_std], axis=1)
for t in cases:
    result = t.aggregate({"A": np.mean, "B": np.std})
    tm.assert_frame_equal(result, expected, check_like=True)

    result = t.aggregate(A=("A", np.mean), B=("B", np.std))
    tm.assert_frame_equal(result, expected, check_like=True)

    result = t.aggregate(A=NamedAgg("A", np.mean), B=NamedAgg("B", np.std))
    tm.assert_frame_equal(result, expected, check_like=True)

expected = pd.concat([a_mean, a_std], axis=1)
expected.columns = pd.MultiIndex.from_tuples([("A", "mean"), ("A", "std")])
for t in cases:
    result = t.aggregate({"A": ["mean", "std"]})
    tm.assert_frame_equal(result, expected)

expected = pd.concat([a_mean, a_sum], axis=1)
expected.columns = ["mean", "sum"]
for t in cases:
    result = t["A"].aggregate(["mean", "sum"])
    tm.assert_frame_equal(result, expected)

    result = t["A"].aggregate(mean="mean", sum="sum")
    tm.assert_frame_equal(result, expected)

msg = "nested renamer is not supported"
for t in cases:
    with pytest.raises(pd.errors.SpecificationError, match=msg):
        t.aggregate({"A": {"mean": "mean", "sum": "sum"}})

expected = pd.concat([a_mean, a_sum, b_mean, b_sum], axis=1)
expected.columns = pd.MultiIndex.from_tuples(
    [("A", "mean"), ("A", "sum"), ("B", "mean2"), ("B", "sum2")]
)
for t in cases:
    with pytest.raises(pd.errors.SpecificationError, match=msg):
        t.aggregate(
            {
                "A": {"mean": "mean", "sum": "sum"},
                "B": {"mean2": "mean", "sum2": "sum"},
            }
        )

expected = pd.concat([a_mean, a_std, b_mean, b_std], axis=1)
expected.columns = pd.MultiIndex.from_tuples(
    [("A", "mean"), ("A", "std"), ("B", "mean"), ("B", "std")]
)
for t in cases:
    result = t.aggregate({"A": ["mean", "std"], "B": ["mean", "std"]})
    tm.assert_frame_equal(result, expected, check_like=True)

expected = pd.concat([a_mean, a_sum, b_mean, b_sum], axis=1)
expected.columns = pd.MultiIndex.from_tuples(
    [
        ("r1", "A", "mean"),
        ("r1", "A", "sum"),
        ("r2", "B", "mean"),
        ("r2", "B", "sum"),
    ]
)
