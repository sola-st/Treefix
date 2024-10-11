# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
# drop_sql = "DROP TABLE IF EXISTS test"  # should already be done
iris_results = self.pandasSQL.execute("SELECT * FROM iris")
row = iris_results.fetchone()
tm.equalContents(row, [5.1, 3.5, 1.4, 0.2, "Iris-setosa"])
