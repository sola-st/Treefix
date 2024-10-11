# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_json_table_schema.py
# GH 18912
df = DataFrame(
    [["Arr", "alpha", [1, 2, 3, 4]], ["Bee", "Beta", [10, 20, 30, 40]]],
    index=[["A", "B"], ["Null", "Eins"]],
    columns=["Aussprache", "Griechisch", "Args"],
)
df.index.names = index_names
out = df.to_json(orient="table")
result = pd.read_json(out, orient="table")
tm.assert_frame_equal(df, result)
