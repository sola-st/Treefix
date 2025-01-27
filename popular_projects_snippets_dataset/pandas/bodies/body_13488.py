# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
frame = tm.makeTimeDataFrame()
create_sql = sql.get_schema(frame, "test")
cur = sqlite_buildin.cursor()
cur.execute(create_sql)
ins = "INSERT INTO test VALUES (?, ?, ?, ?)"

row = frame.iloc[0]
with sql.pandasSQL_builder(sqlite_buildin) as pandas_sql:
    pandas_sql.execute(ins, tuple(row))
sqlite_buildin.commit()

result = sql.read_sql("select * from test", sqlite_buildin)
result.index = frame.index[:1]
tm.assert_frame_equal(result, frame[:1])
