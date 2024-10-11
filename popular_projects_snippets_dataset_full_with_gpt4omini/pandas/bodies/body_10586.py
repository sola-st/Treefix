# Extracted from ./data/repos/pandas/pandas/tests/groupby/aggregate/test_aggregate.py
# GH #1268
grouped = df.groupby("A")

# Expected
d = {"C": {"foo": "mean", "bar": "std"}, "D": {"sum": "sum"}}
# this uses column selection & renaming
msg = r"nested renamer is not supported"
with pytest.raises(SpecificationError, match=msg):
    grouped.aggregate(d)

# Test 1
d = {"C": {"foo": "mean", "bar": "std"}, "D": "sum"}
# this uses column selection & renaming
with pytest.raises(SpecificationError, match=msg):
    grouped.aggregate(d)

# Test 2
d = {"C": {"foo": "mean", "bar": "std"}, "D": "sum"}
# this uses column selection & renaming
with pytest.raises(SpecificationError, match=msg):
    grouped.aggregate(d)
