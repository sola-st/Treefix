# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
iris_frame = sql.read_sql_table(
    "iris", con=self.conn, columns=["SepalLength", "SepalLength"]
)
tm.equalContents(iris_frame.columns.values, ["SepalLength", "SepalLength"])
