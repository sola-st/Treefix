# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
"""`to_sql` with the `engine` param"""
# mostly copied from this class's `_to_sql()` method
self.drop_table("test_frame1", self.conn)

assert (
    self.pandasSQL.to_sql(
        test_frame1, "test_frame1", engine=engine, **engine_kwargs
    )
    == 4
)
assert self.pandasSQL.has_table("test_frame1")

num_entries = len(test_frame1)
num_rows = count_rows(self.conn, "test_frame1")
assert num_rows == num_entries

# Nuke table
self.drop_table("test_frame1", self.conn)
