# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
df = sql.read_sql_table("types", self.conn)

# IMPORTANT - sqlite has no native date type, so shouldn't parse, but
# MySQL SHOULD be converted.
assert issubclass(df.DateCol.dtype.type, np.datetime64)
