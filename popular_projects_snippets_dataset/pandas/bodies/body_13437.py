# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
if isinstance(connectable, Engine):
    with connectable.connect() as conn:
        with conn.begin():
            test_connectable(conn)
else:
    test_connectable(connectable)
