# Extracted from ./data/repos/pandas/pandas/tests/io/test_parquet.py
# GH #34777
# Not supported in fastparquet as of 0.1.3
engine = pa

# Not able to write column multi-indexes with non-string column names
arrays = [
    ["bar", "bar", "baz", "baz", "foo", "foo", "qux", "qux"],
    [1, 2, 1, 2, 1, 2, 1, 2],
]
df = pd.DataFrame(np.random.randn(8, 8), columns=arrays)
df.columns.names = ["Level1", "Level2"]
msg = (
    r"\s*parquet must have string column names for all values in\s*"
    "each level of the MultiIndex"
)
self.check_error_on_write(df, engine, ValueError, msg)
