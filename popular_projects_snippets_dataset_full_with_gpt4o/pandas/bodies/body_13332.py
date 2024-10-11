# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
query = SQL_STRINGS["read_no_parameters_with_percent"][self.flavor]
iris_frame = self.pandasSQL.read_query(query, params=None)
check_iris_frame(iris_frame)
