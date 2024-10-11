# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py

# Test Timestamp objects (no datetime64 because of timezone) (GH9085)
df = DataFrame(
    {"time": to_datetime(["2014-12-12 01:54", "2014-12-11 02:54"], utc=True)}
)
db = sql.SQLiteDatabase(self.conn)
table = sql.SQLiteTable("test_type", db, frame=df)
schema = table.sql_schema()
assert self._get_sqlite_column_type(schema, "time") == "TIMESTAMP"
