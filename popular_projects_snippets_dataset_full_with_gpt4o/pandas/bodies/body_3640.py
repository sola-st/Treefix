# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_drop.py
index = MultiIndex.from_arrays(
    [[0, 0, 0, 1, 1, 1], [1, 2, 3, 1, 2, 3]], names=["one", "two"]
)

df = DataFrame(np.random.randn(6, 3), index=index)

result = df.drop([(0, 2)])
assert result.index.names == ("one", "two")
