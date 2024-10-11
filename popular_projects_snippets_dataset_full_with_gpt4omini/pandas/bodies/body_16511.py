# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_crosstab.py
a = np.random.randint(0, 7, size=100)
b = np.random.randint(0, 3, size=100)
c = np.random.randint(0, 5, size=100)
values = np.random.randn(100)

table = crosstab(
    [a, b], c, values, aggfunc=np.sum, rownames=["foo", "bar"], colnames=["baz"]
)

df = DataFrame({"foo": a, "bar": b, "baz": c, "values": values})

expected = df.pivot_table(
    "values", index=["foo", "bar"], columns="baz", aggfunc=np.sum
)
tm.assert_frame_equal(table, expected)
