# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_concat.py
df = DataFrame(np.random.randn(1, 3))
df2 = DataFrame(np.random.randn(1, 4))

levels = [["foo", "baz"], ["one", "two"]]
names = ["first", "second"]
result = concat(
    [df, df2, df, df2],
    keys=[("foo", "one"), ("foo", "two"), ("baz", "one"), ("baz", "two")],
    levels=levels,
    names=names,
)
expected = concat([df, df2, df, df2])
exp_index = MultiIndex(
    levels=levels + [[0]],
    codes=[[0, 0, 1, 1], [0, 1, 0, 1], [0, 0, 0, 0]],
    names=names + [None],
)
expected.index = exp_index

tm.assert_frame_equal(result, expected)

# no names
result = concat(
    [df, df2, df, df2],
    keys=[("foo", "one"), ("foo", "two"), ("baz", "one"), ("baz", "two")],
    levels=levels,
)
assert result.index.names == (None,) * 3

# no levels
result = concat(
    [df, df2, df, df2],
    keys=[("foo", "one"), ("foo", "two"), ("baz", "one"), ("baz", "two")],
    names=["first", "second"],
)
assert result.index.names == ("first", "second", None)
tm.assert_index_equal(
    result.index.levels[0], Index(["baz", "foo"], name="first")
)
