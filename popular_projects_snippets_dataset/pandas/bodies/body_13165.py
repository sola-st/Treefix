# Extracted from ./data/repos/pandas/pandas/tests/io/test_parquet.py
# GH #34777
# Not supported in fastparquet as of 0.1.3
engine = pa

# Write column multi-indexes with string column names
arrays = [
    ["bar", "bar", "baz", "baz", "foo", "foo", "qux", "qux"],
    ["one", "two", "one", "two", "one", "two", "one", "two"],
]
df = pd.DataFrame(np.random.randn(8, 8), columns=arrays)
df.columns.names = ["ColLevel1", "ColLevel2"]

check_round_trip(df, engine)
