# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
# GH10285 Add dtype argument to read_sql_query
df = DataFrame([[1.2, 3.4], [5.6, 7.8]], columns=["A", "B"])
assert df.to_sql("test_dtype_argument", self.conn) == 2

expected = df.astype(dtype)
result = sql.read_sql_query(
    "SELECT A, B FROM test_dtype_argument", con=self.conn, dtype=dtype
)

tm.assert_frame_equal(result, expected)
