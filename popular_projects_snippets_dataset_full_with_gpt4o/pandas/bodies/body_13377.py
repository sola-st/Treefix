# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
from sqlalchemy import TIMESTAMP

# Test Timestamp objects (no datetime64 because of timezone) (GH9085)
df = DataFrame(
    {"time": to_datetime(["2014-12-12 01:54", "2014-12-11 02:54"], utc=True)}
)
db = sql.SQLDatabase(self.conn)
table = sql.SQLTable("test_type", db, frame=df)
# GH 9086: TIMESTAMP is the suggested type for datetimes with timezones
assert isinstance(table.table.c["time"].type, TIMESTAMP)
