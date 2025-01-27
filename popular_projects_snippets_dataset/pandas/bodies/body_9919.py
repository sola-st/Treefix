# Extracted from ./data/repos/pandas/pandas/tests/window/test_api.py

# API change for disallowing these types of nested dicts
df = DataFrame({"A": range(5), "B": range(0, 10, 2)})
r = df.rolling(window=3)

msg = "nested renamer is not supported"
with pytest.raises(SpecificationError, match=msg):
    r.aggregate({"r1": {"A": ["mean", "sum"]}, "r2": {"B": ["mean", "sum"]}})

expected = concat(
    [r["A"].mean(), r["A"].std(), r["B"].mean(), r["B"].std()], axis=1
)
expected.columns = MultiIndex.from_tuples(
    [("ra", "mean"), ("ra", "std"), ("rb", "mean"), ("rb", "std")]
)
with pytest.raises(SpecificationError, match=msg):
    r[["A", "B"]].agg({"A": {"ra": ["mean", "std"]}, "B": {"rb": ["mean", "std"]}})

with pytest.raises(SpecificationError, match=msg):
    r.agg({"A": {"ra": ["mean", "std"]}, "B": {"rb": ["mean", "std"]}})
