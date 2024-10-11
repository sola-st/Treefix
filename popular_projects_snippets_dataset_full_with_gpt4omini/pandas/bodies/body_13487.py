# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
frame = tm.makeTimeDataFrame()
frame.iloc[0, 0] = np.nan
create_sql = sql.get_schema(frame, "test")
cur = sqlite_buildin.cursor()
cur.execute(create_sql)

ins = "INSERT INTO test VALUES (%s, %s, %s, %s)"
for _, row in frame.iterrows():
    fmt_sql = format_query(ins, *row)
    tquery(fmt_sql, con=sqlite_buildin)

sqlite_buildin.commit()

result = sql.read_sql("select * from test", con=sqlite_buildin)
result.index = frame.index
tm.assert_frame_equal(result, frame, rtol=1e-3)
