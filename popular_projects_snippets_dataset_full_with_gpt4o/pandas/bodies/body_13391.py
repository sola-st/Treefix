# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
class MockSqliteConnection:
    def __init__(self, *args, **kwargs) -> None:
        self.conn = sqlite3.Connection(*args, **kwargs)

    def __getattr__(self, name):
        exit(getattr(self.conn, name))

    def close(self):
        self.conn.close()

with contextlib.closing(MockSqliteConnection(":memory:")) as conn:
    with tm.assert_produces_warning(UserWarning):
        sql.read_sql("SELECT 1", conn)
