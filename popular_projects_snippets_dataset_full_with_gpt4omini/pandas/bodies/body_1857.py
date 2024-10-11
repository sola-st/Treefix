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

# passed lambda
for t in cases:
    result = t.agg({"A": np.sum, "B": lambda x: np.std(x, ddof=1)})
    rcustom = t["B"].apply(lambda x: np.std(x, ddof=1))
    expected = pd.concat([r["A"].sum(), rcustom], axis=1)
    tm.assert_frame_equal(result, expected, check_like=True)

    result = t.agg(A=("A", np.sum), B=("B", lambda x: np.std(x, ddof=1)))
    tm.assert_frame_equal(result, expected, check_like=True)

    result = t.agg(
        A=NamedAgg("A", np.sum), B=NamedAgg("B", lambda x: np.std(x, ddof=1))
    )
    tm.assert_frame_equal(result, expected, check_like=True)

# agg with renamers
expected = pd.concat(
    [t["A"].sum(), t["B"].sum(), t["A"].mean(), t["B"].mean()], axis=1
)
expected.columns = pd.MultiIndex.from_tuples(
    [("result1", "A"), ("result1", "B"), ("result2", "A"), ("result2", "B")]
)

msg = r"Column\(s\) \['result1', 'result2'\] do not exist"
for t in cases:
    with pytest.raises(KeyError, match=msg):
        t[["A", "B"]].agg({"result1": np.sum, "result2": np.mean})

    with pytest.raises(KeyError, match=msg):
        t[["A", "B"]].agg(A=("result1", np.sum), B=("result2", np.mean))

    with pytest.raises(KeyError, match=msg):
        t[["A", "B"]].agg(
            A=NamedAgg("result1", np.sum), B=NamedAgg("result2", np.mean)
        )

    # agg with different hows
expected = pd.concat(
    [t["A"].sum(), t["A"].std(), t["B"].mean(), t["B"].std()], axis=1
)
expected.columns = pd.MultiIndex.from_tuples(
    [("A", "sum"), ("A", "std"), ("B", "mean"), ("B", "std")]
)
for t in cases:
    result = t.agg({"A": ["sum", "std"], "B": ["mean", "std"]})
    tm.assert_frame_equal(result, expected, check_like=True)

# equivalent of using a selection list / or not
for t in cases:
    result = t[["A", "B"]].agg({"A": ["sum", "std"], "B": ["mean", "std"]})
    tm.assert_frame_equal(result, expected, check_like=True)

msg = "nested renamer is not supported"

# series like aggs
for t in cases:
    with pytest.raises(pd.errors.SpecificationError, match=msg):
        t["A"].agg({"A": ["sum", "std"]})

    with pytest.raises(pd.errors.SpecificationError, match=msg):
        t["A"].agg({"A": ["sum", "std"], "B": ["mean", "std"]})

    # errors
    # invalid names in the agg specification
msg = r"Column\(s\) \['B'\] do not exist"
for t in cases:
    with pytest.raises(KeyError, match=msg):
        t[["A"]].agg({"A": ["sum", "std"], "B": ["mean", "std"]})
