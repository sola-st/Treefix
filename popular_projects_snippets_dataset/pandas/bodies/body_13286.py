# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
from sqlalchemy import insert
from sqlalchemy.engine import Engine

iris = iris_table_metadata(dialect)
iris.drop(conn, checkfirst=True)
iris.create(bind=conn)

with iris_file.open(newline=None) as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)
    params = [dict(zip(header, row)) for row in reader]
    stmt = insert(iris).values(params)
    if isinstance(conn, Engine):
        with conn.connect() as conn:
            with conn.begin():
                conn.execute(stmt)
    else:
        conn.execute(stmt)
