# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
if self.mode == "sqlalchemy":
    from sqlalchemy import Integer

    dtype = Integer
else:
    dtype = "INTEGER"

float_frame = DataFrame({"a": [1.1, 1.2], "b": [2.1, 2.2]})
create_sql = sql.get_schema(
    float_frame, "test", con=self.conn, dtype={"b": dtype}
)
assert "CREATE" in create_sql
assert "INTEGER" in create_sql
