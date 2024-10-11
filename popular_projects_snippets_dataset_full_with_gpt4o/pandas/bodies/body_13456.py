# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
# test no warning for BIGINT (to support int64) is raised (GH7433)
df = DataFrame({"a": [1, 2]}, dtype="int64")
assert df.to_sql("test_bigintwarning", self.conn, index=False) == 2

with tm.assert_produces_warning(None):
    sql.read_sql_table("test_bigintwarning", self.conn)
