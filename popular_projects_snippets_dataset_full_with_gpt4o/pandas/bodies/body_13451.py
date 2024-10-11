# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
# GH#50797
table = "test"
df = DataFrame({"a": [1, 2, 3], "b": 5})
df.to_sql(table, self.conn, index=False, if_exists="replace")

result = getattr(pd, func)(
    f"Select * from {table}",
    self.conn,
    dtype={"a": np.float64},
    use_nullable_dtypes=use_nullable_dtypes,
)
expected = DataFrame(
    {
        "a": Series([1, 2, 3], dtype=np.float64),
        "b": Series(
            [5, 5, 5], dtype="int64" if not use_nullable_dtypes else "Int64"
        ),
    }
)
tm.assert_frame_equal(result, expected)
