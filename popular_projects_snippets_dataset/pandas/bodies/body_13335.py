# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
self.drop_table("test_frame_roundtrip", self.conn)
assert self.pandasSQL.to_sql(test_frame1, "test_frame_roundtrip") == 4
result = self.pandasSQL.read_query("SELECT * FROM test_frame_roundtrip")

result.set_index("level_0", inplace=True)
# result.index.astype(int)

result.index.name = None

tm.assert_frame_equal(result, test_frame1)
