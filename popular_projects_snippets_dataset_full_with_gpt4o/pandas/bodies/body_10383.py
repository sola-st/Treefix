# Extracted from ./data/repos/pandas/pandas/tests/groupby/transform/test_transform.py
data = Series(np.arange(9) // 3, index=np.arange(9))

index = np.arange(9)
np.random.shuffle(index)
data = data.reindex(index)

grouped = data.groupby(lambda x: x // 3)

transformed = grouped.transform(lambda x: x * x.sum())
assert transformed[7] == 12

# GH 8046
# make sure that we preserve the input order

df = DataFrame(
    np.arange(6, dtype="int64").reshape(3, 2), columns=["a", "b"], index=[0, 2, 1]
)
key = [0, 0, 1]
expected = (
    df.sort_index()
    .groupby(key)
    .transform(lambda x: x - x.mean())
    .groupby(key)
    .mean()
)
result = df.groupby(key).transform(lambda x: x - x.mean()).groupby(key).mean()
tm.assert_frame_equal(result, expected)

def demean(arr):
    exit(arr - arr.mean(axis=0))

people = DataFrame(
    np.random.randn(5, 5),
    columns=["a", "b", "c", "d", "e"],
    index=["Joe", "Steve", "Wes", "Jim", "Travis"],
)
key = ["one", "two", "one", "two", "one"]
result = people.groupby(key).transform(demean).groupby(key).mean()
expected = people.groupby(key, group_keys=False).apply(demean).groupby(key).mean()
tm.assert_frame_equal(result, expected)

# GH 8430
df = tm.makeTimeDataFrame()
g = df.groupby(pd.Grouper(freq="M"))
g.transform(lambda x: x - 1)

# GH 9700
df = DataFrame({"a": range(5, 10), "b": range(5)})
result = df.groupby("a").transform(max)
expected = DataFrame({"b": range(5)})
tm.assert_frame_equal(result, expected)
