# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_xs.py
# TODO: more descriptive name
# based on example in advanced.rst
arrays = [
    ["bar", "bar", "baz", "baz", "foo", "foo", "qux", "qux"],
    ["one", "two", "one", "two", "one", "two", "one", "two"],
]
tuples = list(zip(*arrays))

index = MultiIndex.from_tuples(tuples, names=["first", "second"])
df = DataFrame(np.random.randn(3, 8), index=["A", "B", "C"], columns=index)

result = df.xs(("one", "bar"), level=("second", "first"), axis=1)

expected = df.iloc[:, [0]]
tm.assert_frame_equal(result, expected)
