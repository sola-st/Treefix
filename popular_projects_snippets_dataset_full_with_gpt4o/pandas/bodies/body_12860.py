# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_json_table_schema_ext_dtype.py
# GH#40255
df = DataFrame(
    {
        "a": Series([2, NA], dtype="Int64"),
        "b": Series([1.5, NA], dtype="Float64"),
        "c": Series([True, NA], dtype="boolean"),
    },
    index=Index([1, NA], dtype="Int64"),
)
expected = df.copy()
data_json = df.to_json(orient="table", indent=4)
result = read_json(data_json, orient="table")
tm.assert_frame_equal(result, expected)
