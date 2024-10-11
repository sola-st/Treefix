# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
# test support for datetime.time
df = DataFrame([time(9, 0, 0), time(9, 1, 30)], columns=["a"])
assert df.to_sql("test_time", self.conn, index=False) == 2
res = read_sql_table("test_time", self.conn)
tm.assert_frame_equal(res, df)

# GH8341
# first, use the fallback to have the sqlite adapter put in place
sqlite_conn = sqlite_buildin
assert sql.to_sql(df, "test_time2", sqlite_conn, index=False) == 2
res = sql.read_sql_query("SELECT * FROM test_time2", sqlite_conn)
ref = df.applymap(lambda _: _.strftime("%H:%M:%S.%f"))
tm.assert_frame_equal(ref, res)  # check if adapter is in place
# then test if sqlalchemy is unaffected by the sqlite adapter
assert sql.to_sql(df, "test_time3", self.conn, index=False) == 2
if self.flavor == "sqlite":
    res = sql.read_sql_query("SELECT * FROM test_time3", self.conn)
    ref = df.applymap(lambda _: _.strftime("%H:%M:%S.%f"))
    tm.assert_frame_equal(ref, res)
res = sql.read_sql_table("test_time3", self.conn)
tm.assert_frame_equal(df, res)
