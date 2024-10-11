# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
frame = tm.makeTimeDataFrame()
assert (
    sql.to_sql(frame, name="test_table", con=sqlite_buildin, index=False) == 30
)
result = sql.read_sql("select * from test_table", sqlite_buildin)

# HACK! Change this once indexes are handled properly.
result.index = frame.index

expected = frame
tm.assert_frame_equal(result, frame)

frame["txt"] = ["a"] * len(frame)
frame2 = frame.copy()
new_idx = Index(np.arange(len(frame2)), dtype=np.int64) + 10
frame2["Idx"] = new_idx.copy()
assert (
    sql.to_sql(frame2, name="test_table2", con=sqlite_buildin, index=False)
    == 30
)
result = sql.read_sql(
    "select * from test_table2", sqlite_buildin, index_col="Idx"
)
expected = frame.copy()
expected.index = new_idx
expected.index.name = "Idx"
tm.assert_frame_equal(expected, result)
