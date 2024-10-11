# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
# see gh-7815
with tm.assert_produces_warning(
    UserWarning,
    match=(
        r"The provided table name 'TABLE1' is not found exactly as such in "
        r"the database after writing the table, possibly due to case "
        r"sensitivity issues. Consider using lower case table names."
    ),
):
    sql.SQLDatabase(self.conn).check_case_sensitive("TABLE1", "")

# Test that the warning is certainly NOT triggered in a normal case.
with tm.assert_produces_warning(None):
    test_frame1.to_sql("CaseSensitive", self.conn)
