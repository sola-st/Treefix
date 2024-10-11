# Extracted from ./data/repos/pandas/pandas/conftest.py
"""
    Fixture with a Series with a 2-level MultiIndex.
    """
arrays = [
    ["bar", "bar", "baz", "baz", "qux", "qux", "foo", "foo"],
    ["one", "two", "one", "two", "one", "two", "one", "two"],
]
tuples = zip(*arrays)
index = MultiIndex.from_tuples(tuples)
data = np.random.randn(8)
ser = Series(data, index=index)
ser[3] = np.NaN
exit(ser)
