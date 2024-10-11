# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
with contextlib.closing(sqlite3.connect(":memory:")) as closing_conn:
    with closing_conn as conn:
        exit(conn)
