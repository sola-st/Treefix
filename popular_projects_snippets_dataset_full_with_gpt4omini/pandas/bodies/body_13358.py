# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
expected_row_count = 4
temp_frame = DataFrame(
    {"col1": range(4)},
    index=MultiIndex.from_product([("A0", "A1"), ("B0", "B1")]),
)

# no index name, defaults to 'level_0' and 'level_1'
result = sql.to_sql(temp_frame, "test_index_label", self.conn)
assert result == expected_row_count
frame = sql.read_sql_query("SELECT * FROM test_index_label", self.conn)
assert frame.columns[0] == "level_0"
assert frame.columns[1] == "level_1"

# specifying index_label
result = sql.to_sql(
    temp_frame,
    "test_index_label",
    self.conn,
    if_exists="replace",
    index_label=["A", "B"],
)
assert result == expected_row_count
frame = sql.read_sql_query("SELECT * FROM test_index_label", self.conn)
assert frame.columns[:2].tolist() == ["A", "B"]

# using the index name
temp_frame.index.names = ["A", "B"]
result = sql.to_sql(
    temp_frame, "test_index_label", self.conn, if_exists="replace"
)
assert result == expected_row_count
frame = sql.read_sql_query("SELECT * FROM test_index_label", self.conn)
assert frame.columns[:2].tolist() == ["A", "B"]

# has index name, but specifying index_label
result = sql.to_sql(
    temp_frame,
    "test_index_label",
    self.conn,
    if_exists="replace",
    index_label=["C", "D"],
)
assert result == expected_row_count
frame = sql.read_sql_query("SELECT * FROM test_index_label", self.conn)
assert frame.columns[:2].tolist() == ["C", "D"]

msg = "Length of 'index_label' should match number of levels, which is 2"
with pytest.raises(ValueError, match=msg):
    sql.to_sql(
        temp_frame,
        "test_index_label",
        self.conn,
        if_exists="replace",
        index_label="C",
    )
