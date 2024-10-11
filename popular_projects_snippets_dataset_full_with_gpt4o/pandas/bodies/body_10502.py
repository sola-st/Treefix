# Extracted from ./data/repos/pandas/pandas/tests/groupby/aggregate/test_other.py
# GH 12334
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
    g["D"].agg({"C": ["sum", "std"]})

with pytest.raises(SpecificationError, match=msg):
    g["D"].agg({"C": "sum", "D": "std"})
