# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
self.conn = self.connect()
self.load_iris_data(iris_path)
self.load_types_data(types_data)
self.pandasSQL = sql.SQLiteDatabase(self.conn)
