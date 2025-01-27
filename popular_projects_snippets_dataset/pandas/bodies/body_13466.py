# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
from sqlalchemy.engine import Engine

# only test this for postgresql (schema's not supported in
# mysql/sqlite)
df = DataFrame({"col1": [1, 2], "col2": [0.1, 0.2], "col3": ["a", "n"]})

# create a schema
self.conn.execute("DROP SCHEMA IF EXISTS other CASCADE;")
self.conn.execute("CREATE SCHEMA other;")

# write dataframe to different schema's
assert df.to_sql("test_schema_public", self.conn, index=False) == 2
assert (
    df.to_sql(
        "test_schema_public_explicit", self.conn, index=False, schema="public"
    )
    == 2
)
assert (
    df.to_sql("test_schema_other", self.conn, index=False, schema="other") == 2
)

# read dataframes back in
res1 = sql.read_sql_table("test_schema_public", self.conn)
tm.assert_frame_equal(df, res1)
res2 = sql.read_sql_table("test_schema_public_explicit", self.conn)
tm.assert_frame_equal(df, res2)
res3 = sql.read_sql_table(
    "test_schema_public_explicit", self.conn, schema="public"
)
tm.assert_frame_equal(df, res3)
res4 = sql.read_sql_table("test_schema_other", self.conn, schema="other")
tm.assert_frame_equal(df, res4)
msg = "Table test_schema_other not found"
with pytest.raises(ValueError, match=msg):
    sql.read_sql_table("test_schema_other", self.conn, schema="public")

# different if_exists options

# create a schema
self.conn.execute("DROP SCHEMA IF EXISTS other CASCADE;")
self.conn.execute("CREATE SCHEMA other;")

# write dataframe with different if_exists options
assert (
    df.to_sql("test_schema_other", self.conn, schema="other", index=False) == 2
)
df.to_sql(
    "test_schema_other",
    self.conn,
    schema="other",
    index=False,
    if_exists="replace",
)
assert (
    df.to_sql(
        "test_schema_other",
        self.conn,
        schema="other",
        index=False,
        if_exists="append",
    )
    == 2
)
res = sql.read_sql_table("test_schema_other", self.conn, schema="other")
tm.assert_frame_equal(concat([df, df], ignore_index=True), res)

# specifying schema in user-provided meta

# The schema won't be applied on another Connection
# because of transactional schemas
if isinstance(self.conn, Engine):
    engine2 = self.connect()
    pdsql = sql.SQLDatabase(engine2, schema="other")
    assert pdsql.to_sql(df, "test_schema_other2", index=False) == 2
    assert (
        pdsql.to_sql(df, "test_schema_other2", index=False, if_exists="replace")
        == 2
    )
    assert (
        pdsql.to_sql(df, "test_schema_other2", index=False, if_exists="append")
        == 2
    )
    res1 = sql.read_sql_table("test_schema_other2", self.conn, schema="other")
    res2 = pdsql.read_table("test_schema_other2")
    tm.assert_frame_equal(res1, res2)
