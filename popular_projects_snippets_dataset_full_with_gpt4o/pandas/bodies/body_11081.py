# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_groupby.py
grouped = df.groupby("A")

result = grouped.mean(numeric_only=True)
assert result.index.name == "A"

result = df.groupby("A", as_index=False).mean(numeric_only=True)
assert result.index.name != "A"

result = grouped[["C", "D"]].agg(np.mean)
assert result.index.name == "A"

result = grouped.agg({"C": np.mean, "D": np.std})
assert result.index.name == "A"

result = grouped["C"].mean()
assert result.index.name == "A"
result = grouped["C"].agg(np.mean)
assert result.index.name == "A"
result = grouped["C"].agg([np.mean, np.std])
assert result.index.name == "A"

msg = r"nested renamer is not supported"
with pytest.raises(SpecificationError, match=msg):
    grouped["C"].agg({"foo": np.mean, "bar": np.std})
