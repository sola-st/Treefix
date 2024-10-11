# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
with conn.begin():
    sql.SQLDatabase(conn).drop_table(table_name)
