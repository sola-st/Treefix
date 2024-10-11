# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
# full NaN column (numeric float column)
df = DataFrame({"A": [0, 1, 2], "B": [np.nan, np.nan, np.nan]})
assert df.to_sql("test_nan", self.conn, index=False) == 3

# with read_table
result = sql.read_sql_table("test_nan", self.conn)
tm.assert_frame_equal(result, df)

# with read_sql -> not type info from table -> stays None
df["B"] = df["B"].astype("object")
df["B"] = None
result = sql.read_sql_query("SELECT * FROM test_nan", self.conn)
tm.assert_frame_equal(result, df)
