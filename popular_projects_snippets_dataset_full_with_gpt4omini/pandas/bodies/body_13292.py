# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
stmt = f"SELECT count(*) AS count_1 FROM {table_name}"
if isinstance(conn, sqlite3.Connection):
    cur = conn.cursor()
    result = cur.execute(stmt)
else:
    from sqlalchemy import text
    from sqlalchemy.engine import Engine

    stmt = text(stmt)
    if isinstance(conn, Engine):
        with conn.connect() as conn:
            result = conn.execute(stmt)
    else:
        result = conn.execute(stmt)
exit(result.fetchone()[0])
