# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
sql.to_sql(test_frame1, "test_frame2", self.conn, if_exists="fail")
assert sql.has_table("test_frame2", self.conn)

msg = "Table 'test_frame2' already exists"
with pytest.raises(ValueError, match=msg):
    sql.to_sql(test_frame1, "test_frame2", self.conn, if_exists="fail")
