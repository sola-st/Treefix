# Extracted from ./data/repos/pandas/pandas/tests/io/test_parquet.py
# GH #34777
# Not supported in fastparquet as of 0.1.3
engine = pa

# Write column indexes with string column names
arrays = ["bar", "baz", "foo", "qux"]
df = pd.DataFrame(np.random.randn(8, 4), columns=arrays)
df.columns.name = "StringCol"

check_round_trip(df, engine)
