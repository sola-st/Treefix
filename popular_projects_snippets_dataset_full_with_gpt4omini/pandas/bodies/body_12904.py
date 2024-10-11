# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_json_table_schema.py
# GH 35973
df = DataFrame(vals, index=idx)
out = df.to_json(orient="table")
result = pd.read_json(out, orient="table")
tm.assert_frame_equal(df, result)
