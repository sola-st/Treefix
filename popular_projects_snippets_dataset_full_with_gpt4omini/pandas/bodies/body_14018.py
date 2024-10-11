# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_series_info.py
# GH 14308
# memory usage introspection should not materialize .values
N = 100
M = len(uppercase)
index = MultiIndex.from_product(
    [list(uppercase), date_range("20160101", periods=N)],
    names=["id", "date"],
)
s = Series(np.random.randn(N * M), index=index)

unstacked = s.unstack("id")
assert s.values.nbytes == unstacked.values.nbytes
assert s.memory_usage(deep=True) > unstacked.memory_usage(deep=True).sum()

# high upper bound
diff = unstacked.memory_usage(deep=True).sum() - s.memory_usage(deep=True)
assert diff < 2000
