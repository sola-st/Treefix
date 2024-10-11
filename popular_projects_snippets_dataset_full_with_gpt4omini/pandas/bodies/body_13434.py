# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
query = "SELECT test_foo_data FROM test_foo_data"
exit(sql.read_sql_query(query, con=connection))
