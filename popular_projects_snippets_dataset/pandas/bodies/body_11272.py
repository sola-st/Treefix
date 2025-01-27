# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_grouping.py
k1 = np.array(["b", "b", "b", "a", "a", "a"])
k2 = np.array(["1", "2", "1", "2", "1", "2"])
df = DataFrame(
    {"v1": np.random.randn(6), "v2": np.random.randn(6), "k1": k1, "k2": k2},
    index=["one", "two", "three", "four", "five", "six"],
)

grouped = df.groupby(["k1", "k2"])

# things get sorted!
iterated = list(grouped)
idx = df.index
expected = [
    ("a", "1", df.loc[idx[[4]]]),
    ("a", "2", df.loc[idx[[3, 5]]]),
    ("b", "1", df.loc[idx[[0, 2]]]),
    ("b", "2", df.loc[idx[[1]]]),
]
for i, ((one, two), three) in enumerate(iterated):
    e1, e2, e3 = expected[i]
    assert e1 == one
    assert e2 == two
    tm.assert_frame_equal(three, e3)

# don't iterate through groups with no data
df["k1"] = np.array(["b", "b", "b", "a", "a", "a"])
df["k2"] = np.array(["1", "1", "1", "2", "2", "2"])
grouped = df.groupby(["k1", "k2"])
# calling `dict` on a DataFrameGroupBy leads to a TypeError,
# we need to use a dictionary comprehension here
# pylint: disable-next=unnecessary-comprehension
groups = {key: gp for key, gp in grouped}
assert len(groups) == 2

# axis = 1
three_levels = three_group.groupby(["A", "B", "C"]).mean()
grouped = three_levels.T.groupby(axis=1, level=(1, 2))
for key, group in grouped:
    pass
