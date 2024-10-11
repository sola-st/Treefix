# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
from sqlalchemy import text
from sqlalchemy.engine import Engine

# create invalid table
query_list = [
    text("CREATE TABLE invalid (x INTEGER, y UNKNOWN);"),
    text("CREATE TABLE other_table (x INTEGER, y INTEGER);"),
]
for query in query_list:
    if isinstance(self.conn, Engine):
        with self.conn.connect() as conn:
            with conn.begin():
                conn.execute(query)
    else:
        self.conn.execute(query)

with tm.assert_produces_warning(None):
    sql.read_sql_table("other_table", self.conn)
    sql.read_sql_query("SELECT * FROM other_table", self.conn)
