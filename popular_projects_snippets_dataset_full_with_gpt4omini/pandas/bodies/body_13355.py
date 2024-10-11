# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py

# see #6921
df = to_timedelta(Series(["00:00:01", "00:00:03"], name="foo")).to_frame()
with tm.assert_produces_warning(UserWarning):
    result_count = df.to_sql("test_timedelta", self.conn)
assert result_count == 2
result = sql.read_sql_query("SELECT * FROM test_timedelta", self.conn)
tm.assert_series_equal(result["foo"], df["foo"].view("int64"))
