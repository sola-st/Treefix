# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
try:
    self.conn = self.engine.connect()
    self.conn.begin()
    self.pandasSQL = sql.SQLDatabase(self.conn)
except sqlalchemy.exc.OperationalError:
    pytest.skip(f"Can't connect to {self.flavor} server")
self.load_iris_data(iris_path)
self.load_types_data(types_data)
