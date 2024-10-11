# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_json_table_schema_ext_dtype.py
df = DataFrame(
    {
        "A": DateArray([dt.date(2021, 10, 10)]),
        "B": DecimalArray([decimal.Decimal(10)]),
        "C": array(["pandas"], dtype="string"),
        "D": array([10], dtype="Int64"),
    }
)
result = build_table_schema(df, version=False)
expected = {
    "fields": [
        {"name": "index", "type": "integer"},
        {"name": "A", "type": "any", "extDtype": "DateDtype"},
        {"name": "B", "type": "number", "extDtype": "decimal"},
        {"name": "C", "type": "any", "extDtype": "string"},
        {"name": "D", "type": "integer", "extDtype": "Int64"},
    ],
    "primaryKey": ["index"],
}
assert result == expected
result = build_table_schema(df)
assert "pandas_version" in result
