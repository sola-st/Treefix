# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
s = Series(np.arange(5, dtype="int64"), name="series")
sql.to_sql(s, "test_series", self.conn, index=False)
s2 = sql.read_sql_query("SELECT * FROM test_series", self.conn)
tm.assert_frame_equal(s.to_frame(), s2)
