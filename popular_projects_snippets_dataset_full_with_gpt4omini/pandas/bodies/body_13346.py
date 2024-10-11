# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
assert sql.to_sql(test_frame1, "test_frame4", self.conn, if_exists="fail") == 4

# Add to table again
assert (
    sql.to_sql(test_frame1, "test_frame4", self.conn, if_exists="append") == 4
)
assert sql.has_table("test_frame4", self.conn)

num_entries = 2 * len(test_frame1)
num_rows = count_rows(self.conn, "test_frame4")

assert num_rows == num_entries
