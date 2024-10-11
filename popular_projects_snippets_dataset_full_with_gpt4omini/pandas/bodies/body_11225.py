# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_grouping.py
# GH7511
df = DataFrame(
    columns=["A", "B", "A", "C"], data=[range(4), range(2, 6), range(0, 8, 2)]
)

msg = "Grouper for 'A' not 1-dimensional"
with pytest.raises(ValueError, match=msg):
    df.groupby("A")
with pytest.raises(ValueError, match=msg):
    df.groupby(["A", "B"])

grouped = df.groupby("B")
c = grouped.count()
assert c.columns.nlevels == 1
assert c.columns.size == 3
