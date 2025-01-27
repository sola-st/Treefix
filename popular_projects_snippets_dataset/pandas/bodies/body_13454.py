# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
df = sql.read_sql_table("types", self.conn)

assert issubclass(df.FloatCol.dtype.type, np.floating)
assert issubclass(df.IntCol.dtype.type, np.integer)

# sqlite has no boolean type, so integer type is returned
assert issubclass(df.BoolCol.dtype.type, np.integer)

# Int column with NA values stays as float
assert issubclass(df.IntColWithNull.dtype.type, np.floating)

# Non-native Bool column with NA values stays as float
assert issubclass(df.BoolColWithNull.dtype.type, np.floating)
