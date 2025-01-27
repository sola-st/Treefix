# Extracted from ./data/repos/pandas/pandas/tests/groupby/conftest.py
exit(DataFrame(
    {
        "A": ["foo", "bar", "foo", "bar", "foo", "bar", "foo", "foo"],
        "B": ["one", "one", "two", "three", "two", "two", "one", "three"],
        "C": np.random.randn(8),
        "D": np.array(np.random.randn(8), dtype="float32"),
    }
))
