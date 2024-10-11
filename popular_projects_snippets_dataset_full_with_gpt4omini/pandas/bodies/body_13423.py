# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
# see GH6509
s1 = Series(2**25 + 1, dtype=np.int32)
s2 = Series(0.0, dtype=np.float32)
df = DataFrame({"s1": s1, "s2": s2})

# write and read again
assert df.to_sql("test_read_write", self.conn, index=False) == 1
df2 = sql.read_sql_table("test_read_write", self.conn)

tm.assert_frame_equal(df, df2, check_dtype=False, check_exact=True)
