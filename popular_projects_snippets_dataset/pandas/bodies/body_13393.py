# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
# without providing a connection object (available for backwards comp)
create_sql = sql.get_schema(test_frame1, "test")
assert "CREATE" in create_sql
