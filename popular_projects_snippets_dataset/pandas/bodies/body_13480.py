# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
if self.flavor == "mysql":
    pytest.skip("Not applicable to MySQL legacy")
cols = ["A", "B"]
data = [(0.8, True), (0.9, None)]
df = DataFrame(data, columns=cols)
assert df.to_sql("dtype_test", self.conn) == 2
assert df.to_sql("dtype_test2", self.conn, dtype={"B": "STRING"}) == 2

# sqlite stores Boolean values as INTEGER
assert self._get_sqlite_column_type("dtype_test", "B") == "INTEGER"

assert self._get_sqlite_column_type("dtype_test2", "B") == "STRING"
msg = r"B \(<class 'bool'>\) not a string"
with pytest.raises(ValueError, match=msg):
    df.to_sql("error", self.conn, dtype={"B": bool})

# single dtype
assert df.to_sql("single_dtype_test", self.conn, dtype="STRING") == 2
assert self._get_sqlite_column_type("single_dtype_test", "A") == "STRING"
assert self._get_sqlite_column_type("single_dtype_test", "B") == "STRING"
