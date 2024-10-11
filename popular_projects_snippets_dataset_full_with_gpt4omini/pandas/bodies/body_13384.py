# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
# GH 37157
df = DataFrame({"A": [0, 1, 2], "%_variation": [3, 4, 5]})
df.to_sql("test_column_percentage", self.conn, index=False)

res = sql.read_sql_table("test_column_percentage", self.conn)

tm.assert_frame_equal(res, df)
