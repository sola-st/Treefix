# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
sql.to_sql(test_frame1, "test_frame_roundtrip", con=self.conn)
result = sql.read_sql_query("SELECT * FROM test_frame_roundtrip", con=self.conn)

# HACK!
result.index = test_frame1.index
result.set_index("level_0", inplace=True)
result.index.astype(int)
result.index.name = None
tm.assert_frame_equal(result, test_frame1)
