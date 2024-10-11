# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
# Test if the IO in the database still work if the connection closed
# between the writing and reading (as in many real situations).

with tm.ensure_clean() as name:

    with closing(self.connect(name)) as conn:
        assert (
            sql.to_sql(test_frame3, "test_frame3_legacy", conn, index=False)
            == 4
        )

    with closing(self.connect(name)) as conn:
        result = sql.read_sql_query("SELECT * FROM test_frame3_legacy;", conn)

tm.assert_frame_equal(test_frame3, result)
