# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
query = SQL_STRINGS["read_named_parameters"][self.flavor]
params = {"name": "Iris-setosa", "length": 5.1}
iris_frame = self.pandasSQL.read_query(query, params=params)
check_iris_frame(iris_frame)
