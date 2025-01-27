# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
df = DataFrame([[1, 2], [3, 4]], columns=[0, 1])
sql.to_sql(df, "test_frame_integer_col_names", self.conn, if_exists="replace")
