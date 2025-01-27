# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
self.drop_table("iris", self.conn)
if isinstance(self.conn, sqlite3.Connection):
    create_and_load_iris_sqlite3(self.conn, iris_path)
else:
    create_and_load_iris(self.conn, iris_path, self.flavor)
