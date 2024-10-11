# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
# GH#50048
table = "test"
df = self.nullable_data()
df.to_sql(table, self.conn, index=False, if_exists="replace")

with pd.option_context("mode.string_storage", string_storage):
    result = getattr(pd, func)(
        f"Select * from {table}", self.conn, use_nullable_dtypes=True
    )
expected = self.nullable_expected(string_storage)
tm.assert_frame_equal(result, expected)

with pd.option_context("mode.string_storage", string_storage):
    iterator = getattr(pd, func)(
        f"Select * from {table}",
        self.conn,
        use_nullable_dtypes=True,
        chunksize=3,
    )
    expected = self.nullable_expected(string_storage)
    for result in iterator:
        tm.assert_frame_equal(result, expected)
