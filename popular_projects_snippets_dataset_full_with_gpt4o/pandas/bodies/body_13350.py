# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
sql.to_sql(
    test_frame1,
    "test_frame_roundtrip",
    con=self.conn,
    index=False,
    chunksize=2,
)
result = sql.read_sql_query("SELECT * FROM test_frame_roundtrip", con=self.conn)
tm.assert_frame_equal(result, test_frame1)
