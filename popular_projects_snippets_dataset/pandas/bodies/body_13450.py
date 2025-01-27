# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
# GH#50245
dtypes = {"a": "int64", "b": "object"}
df = DataFrame(columns=["a", "b"]).astype(dtypes)
expected = df.copy()
df.to_sql("test", self.conn, index=False, if_exists="replace")

for result in read_sql_query(
    "SELECT * FROM test",
    self.conn,
    dtype=dtypes,
    chunksize=1,
):
    tm.assert_frame_equal(result, expected)
