# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
from sqlalchemy import insert
from sqlalchemy.engine import Engine

types = types_table_metadata(dialect)
types.drop(conn, checkfirst=True)
types.create(bind=conn)

stmt = insert(types).values(types_data)
if isinstance(conn, Engine):
    with conn.connect() as conn:
        with conn.begin():
            conn.execute(stmt)
else:
    conn.execute(stmt)
