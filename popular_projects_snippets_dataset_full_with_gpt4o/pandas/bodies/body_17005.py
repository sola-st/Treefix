# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_categorical.py

a = Series(np.arange(6, dtype="int64"))
b = Series(list("aabbca"))

df2 = DataFrame(
    {"A": a, "B": b.astype(CategoricalDtype(list("cab")))}
).set_index("B")
result = pd.concat([df2, df2])
expected = DataFrame(
    {
        "A": pd.concat([a, a]),
        "B": pd.concat([b, b]).astype(CategoricalDtype(list("cab"))),
    }
).set_index("B")
tm.assert_frame_equal(result, expected)

# wrong categories -> uses concat_compat, which casts to object
df3 = DataFrame(
    {"A": a, "B": Categorical(b, categories=list("abe"))}
).set_index("B")
result = pd.concat([df2, df3])
expected = pd.concat(
    [
        df2.set_axis(df2.index.astype(object), axis=0),
        df3.set_axis(df3.index.astype(object), axis=0),
    ]
)
tm.assert_frame_equal(result, expected)
