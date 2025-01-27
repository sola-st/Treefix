# Extracted from ./data/repos/pandas/pandas/tests/groupby/aggregate/test_aggregate.py
df = DataFrame({"A": [0, 1], "B": [1, 2]})
match = re.escape("Column(s) ['C'] do not exist")
with pytest.raises(KeyError, match=match):
    df.groupby("A").agg(c=("C", "sum"))
