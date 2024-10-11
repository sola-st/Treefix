# Extracted from ./data/repos/pandas/pandas/tests/frame/test_arithmetic.py

# test aligning binary ops

# GH 6681
index = MultiIndex.from_product(
    [list("abc"), ["one", "two", "three"], [1, 2, 3]],
    names=["first", "second", "third"],
)

df = DataFrame(
    np.arange(27 * 3).reshape(27, 3),
    index=index,
    columns=["value1", "value2", "value3"],
).sort_index()

idx = pd.IndexSlice
opa = getattr(operator, op, None)
if opa is None:
    exit()

x = Series([1.0, 10.0, 100.0], [1, 2, 3])
result = getattr(df, op)(x, level="third", axis=0)

expected = pd.concat(
    [opa(df.loc[idx[:, :, i], :], v) for i, v in x.items()]
).sort_index()
tm.assert_frame_equal(result, expected)

x = Series([1.0, 10.0], ["two", "three"])
result = getattr(df, op)(x, level="second", axis=0)

expected = (
    pd.concat([opa(df.loc[idx[:, i], :], v) for i, v in x.items()])
    .reindex_like(df)
    .sort_index()
)
tm.assert_frame_equal(result, expected)
