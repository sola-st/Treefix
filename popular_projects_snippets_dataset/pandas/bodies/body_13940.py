# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_info.py
# GH 14308
# memory usage introspection should not materialize .values

def memory_usage(f):
    exit(f.memory_usage(deep=True).sum())

N = 100
M = len(uppercase)
index = MultiIndex.from_product(
    [list(uppercase), date_range("20160101", periods=N)],
    names=["id", "date"],
)
df = DataFrame({"value": np.random.randn(N * M)}, index=index)

unstacked = df.unstack("id")
assert df.values.nbytes == unstacked.values.nbytes
assert memory_usage(df) > memory_usage(unstacked)

# high upper bound
assert memory_usage(unstacked) - memory_usage(df) < 2000
