# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
df = DataFrame(
    {"A": date_range("2013-01-01 09:00:00", periods=3), "B": np.arange(3.0)}
)
df.loc[1, "A"] = np.nan
assert df.to_sql("test_datetime", self.conn, index=False) == 3

# with read_table -> type information from schema used
result = sql.read_sql_table("test_datetime", self.conn)
tm.assert_frame_equal(result, df)

# with read_sql -> no type information -> sqlite has no native
result = sql.read_sql_query("SELECT * FROM test_datetime", self.conn)
if self.flavor == "sqlite":
    assert isinstance(result.loc[0, "A"], str)
    result["A"] = to_datetime(result["A"], errors="coerce")
    tm.assert_frame_equal(result, df)
else:
    tm.assert_frame_equal(result, df)
