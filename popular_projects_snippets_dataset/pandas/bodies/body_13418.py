# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
# No Parsing
df = sql.read_sql_table("types", self.conn)
expected_type = object if self.flavor == "sqlite" else np.datetime64
assert issubclass(df.DateCol.dtype.type, expected_type)

df = sql.read_sql_table("types", self.conn, parse_dates=["DateCol"])
assert issubclass(df.DateCol.dtype.type, np.datetime64)

df = sql.read_sql_table(
    "types", self.conn, parse_dates={"DateCol": "%Y-%m-%d %H:%M:%S"}
)
assert issubclass(df.DateCol.dtype.type, np.datetime64)

df = sql.read_sql_table(
    "types",
    self.conn,
    parse_dates={"DateCol": {"format": "%Y-%m-%d %H:%M:%S"}},
)
assert issubclass(df.DateCol.dtype.type, np.datetime64)

df = sql.read_sql_table("types", self.conn, parse_dates=["IntDateCol"])
assert issubclass(df.IntDateCol.dtype.type, np.datetime64)

df = sql.read_sql_table("types", self.conn, parse_dates={"IntDateCol": "s"})
assert issubclass(df.IntDateCol.dtype.type, np.datetime64)

df = sql.read_sql_table(
    "types", self.conn, parse_dates={"IntDateCol": {"unit": "s"}}
)
assert issubclass(df.IntDateCol.dtype.type, np.datetime64)
