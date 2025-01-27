# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_json_table_schema_ext_dtype.py

df = df.copy()
df.index.name = "idx"
result = df.to_json(orient="table", date_format="iso")
result = json.loads(result, object_pairs_hook=OrderedDict)

assert "pandas_version" in result["schema"]
result["schema"].pop("pandas_version")

fields = [
    OrderedDict({"name": "idx", "type": "integer"}),
    OrderedDict({"name": "A", "type": "any", "extDtype": "DateDtype"}),
    OrderedDict({"name": "B", "type": "number", "extDtype": "decimal"}),
    OrderedDict({"name": "C", "type": "any", "extDtype": "string"}),
    OrderedDict({"name": "D", "type": "integer", "extDtype": "Int64"}),
]

schema = OrderedDict({"fields": fields, "primaryKey": ["idx"]})
data = [
    OrderedDict(
        [
            ("idx", 0),
            ("A", "2021-10-10T00:00:00.000"),
            ("B", 10.0),
            ("C", "pandas"),
            ("D", 10),
        ]
    )
]
expected = OrderedDict([("schema", schema), ("data", data)])

assert result == expected
