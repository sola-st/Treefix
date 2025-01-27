# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
stmt = "CREATE VIEW iris_view AS SELECT * FROM iris"
if isinstance(conn, sqlite3.Connection):
    cur = conn.cursor()
    cur.execute(stmt)
else:
    from sqlalchemy import text
    from sqlalchemy.engine import Engine

    stmt = text(stmt)
    if isinstance(conn, Engine):
        with conn.connect() as conn:
            with conn.begin():
                conn.execute(stmt)
    else:
        conn.execute(stmt)
