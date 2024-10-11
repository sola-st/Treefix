# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_pivot.py
data = DataFrame(
    {
        "a": ["bar", "bar", "foo", "foo", "foo"],
        "b": ["one", "two", "one", "one", "two"],
        "c": [1.0, 2.0, 3.0, 3.0, 4.0],
    }
)
with pytest.raises(ValueError, match="duplicate entries"):
    data.pivot(index="a", columns="b", values="c")
