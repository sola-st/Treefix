# Extracted from ./data/repos/pandas/pandas/tests/groupby/aggregate/test_aggregate.py
# GH28426
msg = "Function names"
df = DataFrame({"A": [0, 0, 1, 1], "B": [1, 2, 3, 4]})
with pytest.raises(SpecificationError, match=msg):
    df.groupby("A").agg(["min", "min"])
