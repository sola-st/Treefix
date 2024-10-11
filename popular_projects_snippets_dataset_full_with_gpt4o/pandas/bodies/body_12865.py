# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_json_table_schema.py
s = pd.Series([1, 2, 3], name="foo")
result = build_table_schema(s, version=False)
expected = {
    "fields": [
        {"name": "index", "type": "integer"},
        {"name": "foo", "type": "integer"},
    ],
    "primaryKey": ["index"],
}
assert result == expected
result = build_table_schema(s)
assert "pandas_version" in result
