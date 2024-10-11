# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
sql.to_sql(test_frame1, "test_frame3", self.conn, if_exists="fail")
# Add to table again
sql.to_sql(test_frame1, "test_frame3", self.conn, if_exists="replace")
assert sql.has_table("test_frame3", self.conn)

num_entries = len(test_frame1)
num_rows = count_rows(self.conn, "test_frame3")

assert num_rows == num_entries
