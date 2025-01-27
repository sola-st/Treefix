# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_index.py
a = DataFrame(
    np.random.rand(3, 3),
    columns=list("ABC"),
    index=Index(list("abc"), name="index_a"),
)
b = DataFrame(
    np.random.rand(3, 3),
    columns=list("ABC"),
    index=Index(list("abc"), name="index_b"),
)

result = concat([a, b], keys=["key0", "key1"], names=["lvl0", "lvl1"])

exp = concat([a, b], keys=["key0", "key1"], names=["lvl0"])
names = list(exp.index.names)
names[1] = "lvl1"
exp.index.set_names(names, inplace=True)

tm.assert_frame_equal(result, exp)
assert result.index.names == exp.index.names
