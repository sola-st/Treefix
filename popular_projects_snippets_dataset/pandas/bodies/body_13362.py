# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
create_sql = sql.get_schema(test_frame1, "test", con=self.conn)
assert "CREATE" in create_sql
