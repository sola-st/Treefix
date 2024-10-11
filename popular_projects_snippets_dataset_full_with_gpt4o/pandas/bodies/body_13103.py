# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_writers.py
df = tm.makeDataFrame()
writer = partial(df.to_excel, engine=engine)

reader = partial(pd.read_excel, index_col=0)
result = tm.round_trip_localpath(writer, reader, path=f"foo{ext}")
tm.assert_frame_equal(result, df)
