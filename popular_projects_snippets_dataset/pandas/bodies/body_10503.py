# Extracted from ./data/repos/pandas/pandas/tests/groupby/aggregate/test_other.py
# API change for disallowing these types of nested dicts
df = DataFrame(
    {
        "A": ["foo", "bar", "foo", "bar", "foo", "bar", "foo", "foo"],
        "B": ["one", "one", "two", "two", "two", "two", "one", "two"],
        "C": np.random.randn(8) + 1.0,
        "D": np.arange(8),
    }
)

g = df.groupby(["A", "B"])

msg = r"nested renamer is not supported"
with pytest.raises(SpecificationError, match=msg):
    g.aggregate({"r1": {"C": ["mean", "sum"]}, "r2": {"D": ["mean", "sum"]}})

with pytest.raises(SpecificationError, match=msg):
    g.agg({"C": {"ra": ["mean", "std"]}, "D": {"rb": ["mean", "std"]}})

# same name as the original column
# GH9052
with pytest.raises(SpecificationError, match=msg):
    g["D"].agg({"result1": np.sum, "result2": np.mean})

with pytest.raises(SpecificationError, match=msg):
    g["D"].agg({"D": np.sum, "result2": np.mean})
