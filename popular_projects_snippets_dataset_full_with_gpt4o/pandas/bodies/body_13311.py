# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
conn = request.getfixturevalue(conn)
with pandasSQL_builder(conn) as pandasSQL:
    iris_frame = pandasSQL.read_query("SELECT * FROM iris")
check_iris_frame(iris_frame)
