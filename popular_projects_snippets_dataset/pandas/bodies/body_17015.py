# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_concat.py
df = DataFrame(np.random.randn(10, 4))
pieces = [df.iloc[:, [0, 1]], df.iloc[:, [2]], df.iloc[:, [3]]]
level = ["three", "two", "one", "zero"]
result = concat(
    pieces,
    axis=1,
    keys=["one", "two", "three"],
    levels=[level],
    names=["group_key"],
)

tm.assert_index_equal(result.columns.levels[0], Index(level, name="group_key"))
tm.assert_index_equal(result.columns.levels[1], Index([0, 1, 2, 3]))

assert result.columns.names == ["group_key", None]
