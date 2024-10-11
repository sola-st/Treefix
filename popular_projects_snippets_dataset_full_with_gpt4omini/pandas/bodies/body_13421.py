# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
# test support for datetime.date
df = DataFrame([date(2014, 1, 1), date(2014, 1, 2)], columns=["a"])
assert df.to_sql("test_date", self.conn, index=False) == 2
res = read_sql_table("test_date", self.conn)
result = res["a"]
expected = to_datetime(df["a"])
# comes back as datetime64
tm.assert_series_equal(result, expected)
