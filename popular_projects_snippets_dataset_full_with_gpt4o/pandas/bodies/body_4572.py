# Extracted from ./data/repos/pandas/pandas/tests/test_multilevel.py
midx = MultiIndex(
    levels=[["foo"], ["bar"], ["baz"]],
    codes=[[0], [0], [0]],
    names=["one", "two", "three"],
)
df = DataFrame([np.random.rand(4)], columns=["a", "b", "c", "d"], index=midx)
# should work
df.groupby(level="three")
