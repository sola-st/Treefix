# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
# test columns argument in read_table
sql.to_sql(test_frame1, "test_frame", self.conn)

result = sql.read_sql_table("test_frame", self.conn, index_col="index")
assert result.index.names == ["index"]

result = sql.read_sql_table("test_frame", self.conn, index_col=["A", "B"])
assert result.index.names == ["A", "B"]

result = sql.read_sql_table(
    "test_frame", self.conn, index_col=["A", "B"], columns=["C", "D"]
)
assert result.index.names == ["A", "B"]
assert result.columns.tolist() == ["C", "D"]
