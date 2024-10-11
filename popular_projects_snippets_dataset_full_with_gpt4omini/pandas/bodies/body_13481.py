# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
if self.flavor == "mysql":
    pytest.skip("Not applicable to MySQL legacy")

cols = {
    "Bool": Series([True, None]),
    "Date": Series([datetime(2012, 5, 1), None]),
    "Int": Series([1, None], dtype="object"),
    "Float": Series([1.1, None]),
}
df = DataFrame(cols)

tbl = "notna_dtype_test"
assert df.to_sql(tbl, self.conn) == 2

assert self._get_sqlite_column_type(tbl, "Bool") == "INTEGER"
assert self._get_sqlite_column_type(tbl, "Date") == "TIMESTAMP"
assert self._get_sqlite_column_type(tbl, "Int") == "INTEGER"
assert self._get_sqlite_column_type(tbl, "Float") == "REAL"
