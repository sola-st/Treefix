# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
self.drop_table("test_frame1", self.conn)
assert self.pandasSQL.to_sql(test_frame1.iloc[:0], "test_frame1") == 0
