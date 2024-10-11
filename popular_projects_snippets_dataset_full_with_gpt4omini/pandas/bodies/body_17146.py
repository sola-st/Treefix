# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_pivot.py
# issue #17160
df = DataFrame(
    {
        "foo": ["one", "one", "one", "two", "two", "two"],
        "bar": ["A", "B", "C", "A", "B", "C"],
        "baz": [1, 2, 3, 4, 5, 6],
        "zoo": ["x", "y", "z", "q", "w", "t"],
    }
)

if method:
    result = df.pivot(index="foo", columns="bar", values=values)
else:
    result = pd.pivot(df, index="foo", columns="bar", values=values)

data = [[1, 2, 3, "x", "y", "z"], [4, 5, 6, "q", "w", "t"]]
index = Index(data=["one", "two"], name="foo")
columns = MultiIndex(
    levels=[["baz", "zoo"], ["A", "B", "C"]],
    codes=[[0, 0, 0, 1, 1, 1], [0, 1, 2, 0, 1, 2]],
    names=[None, "bar"],
)
expected = DataFrame(data=data, index=index, columns=columns, dtype="object")
tm.assert_frame_equal(result, expected)
