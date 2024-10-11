# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
iris_frame1 = sql.read_sql_query("SELECT * FROM iris", self.conn)
iris_frame2 = sql.read_sql("SELECT * FROM iris", self.conn)
tm.assert_frame_equal(iris_frame1, iris_frame2)

msg = "Execution failed on sql 'iris': near \"iris\": syntax error"
with pytest.raises(sql.DatabaseError, match=msg):
    sql.read_sql("iris", self.conn)
