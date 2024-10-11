# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_json_table_schema.py
df = df_schema
idx = pd.MultiIndex.from_product([("a", "b"), (1, 2)])
df.index = idx

result = build_table_schema(df, version=False)
expected = {
    "fields": [
        {"name": "level_0", "type": "string"},
        {"name": "level_1", "type": "integer"},
        {"name": "A", "type": "integer"},
        {"name": "B", "type": "string"},
        {"name": "C", "type": "datetime"},
        {"name": "D", "type": "duration"},
    ],
    "primaryKey": ["level_0", "level_1"],
}
assert result == expected

df.index.names = ["idx0", None]
expected["fields"][0]["name"] = "idx0"
expected["primaryKey"] = ["idx0", "level_1"]
result = build_table_schema(df, version=False)
assert result == expected
