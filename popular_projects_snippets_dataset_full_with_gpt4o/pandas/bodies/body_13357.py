# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
temp_frame = DataFrame({"col1": range(4)})
temp_frame.index.name = index_name
query = "SELECT * FROM test_index_label"
sql.to_sql(temp_frame, "test_index_label", self.conn, index_label=index_label)
frame = sql.read_sql_query(query, self.conn)
assert frame.columns[0] == expected
