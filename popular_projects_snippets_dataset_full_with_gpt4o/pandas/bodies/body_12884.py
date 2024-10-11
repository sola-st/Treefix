# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_json_table_schema.py
data = pd.Series(1, index=[1.0, 2.0])
result = data.to_json(orient="table", date_format="iso")
result = json.loads(result, object_pairs_hook=OrderedDict)
result["schema"].pop("pandas_version")

expected = OrderedDict(
    [
        (
            "schema",
            {
                "fields": [
                    {"name": "index", "type": "number"},
                    {"name": "values", "type": "integer"},
                ],
                "primaryKey": ["index"],
            },
        ),
        (
            "data",
            [
                OrderedDict([("index", 1.0), ("values", 1)]),
                OrderedDict([("index", 2.0), ("values", 1)]),
            ],
        ),
    ]
)

assert result == expected
