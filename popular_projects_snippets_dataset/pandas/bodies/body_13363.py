# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
# GH28486
create_sql = sql.get_schema(test_frame1, "test", con=self.conn, schema="pypi")
assert "CREATE TABLE pypi." in create_sql
