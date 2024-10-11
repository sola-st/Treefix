# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
# int64 should be converted to BigInteger, GH7433
df = DataFrame(data={"i64": [2**62]})
assert df.to_sql("test_bigint", self.conn, index=False) == 1
result = sql.read_sql_table("test_bigint", self.conn)

tm.assert_frame_equal(df, result)
