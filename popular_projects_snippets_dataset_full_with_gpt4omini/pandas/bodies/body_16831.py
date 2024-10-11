# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_join.py
# GH #916
df = DataFrame(np.random.randn(20, 6), columns=["a", "b", "c", "d", "e", "f"])
df.insert(0, "id", 0)
df.insert(5, "dt", "foo")

grouped = df.groupby("id")
with pytest.raises(TypeError, match="Could not convert"):
    grouped.mean()
mn = grouped.mean(numeric_only=True)
cn = grouped.count()

# it works!
mn.join(cn, rsuffix="_right")
