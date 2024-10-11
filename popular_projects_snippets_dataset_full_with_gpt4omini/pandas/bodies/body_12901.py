# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_json_table_schema.py
df = DataFrame(vals, index=pd.Index(range(4), name=index_nm))
out = df.to_json(orient="table")
result = pd.read_json(out, orient="table")
tm.assert_frame_equal(df, result)
