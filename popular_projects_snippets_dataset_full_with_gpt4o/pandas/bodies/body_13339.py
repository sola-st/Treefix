# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
self.conn = self.connect()
if not isinstance(self.conn, sqlite3.Connection):
    self.conn.begin()
self.load_iris_data(iris_path)
self.load_types_data(types_data)
self.load_test_data_and_sql()
