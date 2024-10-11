# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
# GH35076 Map pandas integer to optimal SQLAlchemy integer type
df = DataFrame([0, 1], columns=["a"], dtype=integer)
db = sql.SQLDatabase(self.conn)
table = sql.SQLTable("test_type", db, frame=df)

result = str(table.table.c.a.type)
assert result == expected
