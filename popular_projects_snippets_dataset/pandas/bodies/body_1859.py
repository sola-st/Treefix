# Extracted from ./data/repos/pandas/pandas/tests/resample/test_resample_api.py

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

msg = "nested renamer is not supported"
for t in cases:
    with pytest.raises(pd.errors.SpecificationError, match=msg):
        t.aggregate({"r1": {"A": ["mean", "sum"]}, "r2": {"B": ["mean", "sum"]}})

for t in cases:

    with pytest.raises(pd.errors.SpecificationError, match=msg):
        t[["A", "B"]].agg(
            {"A": {"ra": ["mean", "std"]}, "B": {"rb": ["mean", "std"]}}
        )

    with pytest.raises(pd.errors.SpecificationError, match=msg):
        t.agg({"A": {"ra": ["mean", "std"]}, "B": {"rb": ["mean", "std"]}})
