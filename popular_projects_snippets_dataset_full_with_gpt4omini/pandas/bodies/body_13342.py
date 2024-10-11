# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
query = "SELECT * FROM iris_view WHERE SepalLength < 0.0"
with_batch = sql.read_sql_query(query, self.conn, chunksize=5)
without_batch = sql.read_sql_query(query, self.conn)
tm.assert_frame_equal(concat(with_batch), without_batch)
