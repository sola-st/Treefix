# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
sql.to_sql(test_frame1, "test_frame1", self.conn)
assert sql.has_table("test_frame1", self.conn)
