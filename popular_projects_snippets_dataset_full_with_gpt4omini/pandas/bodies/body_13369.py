# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
# GH 13206
df = DataFrame({"A": [0, 1, 2], "B": [0.2, np.nan, 5.6]})
df.to_sql("d1187b08-4943-4c8d-a7f6", self.conn, index=False)

res = sql.read_sql_query("SELECT * FROM `d1187b08-4943-4c8d-a7f6`", self.conn)

tm.assert_frame_equal(res, df)
