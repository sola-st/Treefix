# Extracted from ./data/repos/pandas/pandas/tests/groupby/aggregate/test_aggregate.py
# GH 29422, add test for raises scenario when aggregate column does not exist
df = DataFrame(
    {"group": ["a", "a", "b", "b"], "A": [0, 1, 2, 3], "B": [5, 6, 7, 8]}
)
df.columns = MultiIndex.from_tuples([("x", "group"), ("y", "A"), ("y", "B")])

with pytest.raises(KeyError, match="do not exist"):
    df.groupby(("x", "group")).agg(a=(("Y", "a"), "max"))
