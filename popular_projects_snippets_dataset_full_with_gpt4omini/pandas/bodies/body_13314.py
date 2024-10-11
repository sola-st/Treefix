# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
conn = request.getfixturevalue(conn)
df = sql.read_sql_table("types", conn)

assert issubclass(df.FloatCol.dtype.type, np.floating)
assert issubclass(df.IntCol.dtype.type, np.integer)

# MySQL has no real BOOL type (it's an alias for TINYINT)
assert issubclass(df.BoolCol.dtype.type, np.integer)

# Int column with NA values stays as float
assert issubclass(df.IntColWithNull.dtype.type, np.floating)

# Bool column with NA = int column with NA values => becomes float
assert issubclass(df.BoolColWithNull.dtype.type, np.floating)
