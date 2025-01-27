# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_json_table_schema_ext_dtype.py

s = Series(da, name="a")
s.index.name = "id"
result = s.to_json(orient="table", date_format="iso")
result = json.loads(result, object_pairs_hook=OrderedDict)

assert "pandas_version" in result["schema"]
result["schema"].pop("pandas_version")

fields = [
    {"name": "id", "type": "integer"},
    {"name": "a", "type": "any", "extDtype": "DateDtype"},
]

schema = {"fields": fields, "primaryKey": ["id"]}

expected = OrderedDict(
    [
        ("schema", schema),
        ("data", [OrderedDict([("id", 0), ("a", "2021-10-10T00:00:00.000")])]),
    ]
)

assert result == expected
