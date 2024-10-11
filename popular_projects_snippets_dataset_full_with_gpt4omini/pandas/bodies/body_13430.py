# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
# Use a dataframe without a bool column, since MySQL converts bool to
# TINYINT (which read_sql_table returns as an int and causes a dtype
# mismatch)
from sqlalchemy import text
from sqlalchemy.engine import Engine

tbl = "test_get_schema_create_table"
create_sql = sql.get_schema(test_frame3, tbl, con=self.conn)
blank_test_df = test_frame3.iloc[:0]

self.drop_table(tbl, self.conn)
create_sql = text(create_sql)
if isinstance(self.conn, Engine):
    with self.conn.connect() as conn:
        with conn.begin():
            conn.execute(create_sql)
else:
    self.conn.execute(create_sql)
returned_df = sql.read_sql_table(tbl, self.conn)
tm.assert_frame_equal(returned_df, blank_test_df, check_index_type=False)
self.drop_table(tbl, self.conn)
