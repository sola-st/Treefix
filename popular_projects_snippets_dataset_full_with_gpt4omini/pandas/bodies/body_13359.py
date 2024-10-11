# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
df = DataFrame.from_records(
    [(1, 2.1, "line1"), (2, 1.5, "line2")],
    columns=["A", "B", "C"],
    index=["A", "B"],
)

df.to_sql("test_multiindex_roundtrip", self.conn)
result = sql.read_sql_query(
    "SELECT * FROM test_multiindex_roundtrip", self.conn, index_col=["A", "B"]
)
tm.assert_frame_equal(df, result, check_index_type=True)
