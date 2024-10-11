# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_json_table_schema_ext_dtype.py
s = Series(ia, name="a")
s.index.name = "id"
result = s.to_json(orient="table", date_format="iso")
result = json.loads(result, object_pairs_hook=OrderedDict)

assert "pandas_version" in result["schema"]
result["schema"].pop("pandas_version")

fields = [
    {"name": "id", "type": "integer"},
    {"name": "a", "type": "integer", "extDtype": "Int64"},
]

schema = {"fields": fields, "primaryKey": ["id"]}

expected = OrderedDict(
    [
        ("schema", schema),
        ("data", [OrderedDict([("id", 0), ("a", 10)])]),
    ]
)

assert result == expected
