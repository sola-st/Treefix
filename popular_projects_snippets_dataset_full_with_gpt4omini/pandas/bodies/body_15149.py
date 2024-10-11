# Extracted from ./data/repos/pandas/pandas/tests/series/test_repr.py
biggie = Series(
    np.random.randn(1000), index=np.arange(1000), name=("foo", "bar", "baz")
)
repr(biggie)
