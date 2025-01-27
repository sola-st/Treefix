# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_json_table_schema.py
result = build_table_schema(df_schema, version=False)
expected = {
    "fields": [
        {"name": "idx", "type": "integer"},
        {"name": "A", "type": "integer"},
        {"name": "B", "type": "string"},
        {"name": "C", "type": "datetime"},
        {"name": "D", "type": "duration"},
    ],
    "primaryKey": ["idx"],
}
assert result == expected
result = build_table_schema(df_schema)
assert "pandas_version" in result
