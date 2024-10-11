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
with pytest.raises(KeyError, match=r"^\('bar', 'baz'\)$"):
    # tuple is seen as a single column name
    if method:
        df.pivot(index="zoo", columns="foo", values=("bar", "baz"))
    else:
        pd.pivot(df, index="zoo", columns="foo", values=("bar", "baz"))
