# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
# if setup fails, there may not be a connection to close.
if hasattr(self, "conn"):
    self.conn.close()
# use a fresh connection to ensure we can drop all tables.
try:
    conn = self.connect()
except (sqlalchemy.exc.OperationalError, sqlite3.OperationalError):
    pass
else:
    with conn:
        for tbl in self._get_all_tables(conn):
            self.drop_table(tbl, conn)
