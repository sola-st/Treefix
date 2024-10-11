# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_get_dummies.py
# issue #28383
df = DataFrame(
    {
        "bar": [1, 2, 3, 4, 5, 6],
        "foo": ["one", "one", "one", "two", "two", "two"],
        "baz": ["A", "B", "C", "A", "B", "C"],
        "zoo": ["x", "y", "z", "q", "w", "t"],
    }
)

msg = "Input must be a list-like for parameter `columns`"

with pytest.raises(TypeError, match=msg):
    get_dummies(df, columns=values)
