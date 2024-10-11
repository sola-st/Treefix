# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_json_table_schema.py
result = build_table_schema(pd.Series([1, 2, 3]), version=False)
expected = {
    "fields": [
        {"name": "index", "type": "integer"},
        {"name": "values", "type": "integer"},
    ],
    "primaryKey": ["index"],
}
assert result == expected
