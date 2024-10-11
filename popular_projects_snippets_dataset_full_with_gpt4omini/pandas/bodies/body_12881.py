# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_json_table_schema.py
s = pd.Series([1, 2], name="a")
s.index.name = "id"
result = s.to_json(orient="table", date_format="iso")
result = json.loads(result, object_pairs_hook=OrderedDict)

assert "pandas_version" in result["schema"]
result["schema"].pop("pandas_version")

fields = [{"name": "id", "type": "integer"}, {"name": "a", "type": "integer"}]

schema = {"fields": fields, "primaryKey": ["id"]}

expected = OrderedDict(
    [
        ("schema", schema),
        (
            "data",
            [
                OrderedDict([("id", 0), ("a", 1)]),
                OrderedDict([("id", 1), ("a", 2)]),
            ],
        ),
    ]
)

assert result == expected
