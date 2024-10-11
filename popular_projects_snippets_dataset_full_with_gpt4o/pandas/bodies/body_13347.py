# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
sql.to_sql(test_frame3, "test_frame5", self.conn, index=False)
result = sql.read_sql("SELECT * FROM test_frame5", self.conn)

tm.assert_frame_equal(test_frame3, result)
