# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
# test support for datetime.date
df = DataFrame([date(2014, 1, 1), date(2014, 1, 2)], columns=["a"])
assert df.to_sql("test_date", self.conn, index=False) == 2
res = read_sql_query("SELECT * FROM test_date", self.conn)
if self.flavor == "sqlite":
    # comes back as strings
    tm.assert_frame_equal(res, df.astype(str))
elif self.flavor == "mysql":
    tm.assert_frame_equal(res, df)
