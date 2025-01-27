# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
# test columns argument in read_table
sql.to_sql(test_frame1, "test_frame", self.conn)

cols = ["A", "B"]
result = sql.read_sql_table("test_frame", self.conn, columns=cols)
assert result.columns.tolist() == cols
