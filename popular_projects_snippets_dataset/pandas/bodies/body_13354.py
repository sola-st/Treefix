# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
# Test case where same column appears in parse_date and index_col

df = sql.read_sql_query(
    "SELECT * FROM types",
    self.conn,
    index_col="DateCol",
    parse_dates=["DateCol", "IntDateCol"],
)

assert issubclass(df.index.dtype.type, np.datetime64)
assert issubclass(df.IntDateCol.dtype.type, np.datetime64)
