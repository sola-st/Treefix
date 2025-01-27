# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_json_table_schema.py
data = pd.Series(1, pd.CategoricalIndex(["a", "b"]))
result = data.to_json(orient="table", date_format="iso")
result = json.loads(result, object_pairs_hook=OrderedDict)
result["schema"].pop("pandas_version")

expected = OrderedDict(
    [
        (
            "schema",
            {
                "fields": [
                    {
                        "name": "index",
                        "type": "any",
                        "constraints": {"enum": ["a", "b"]},
                        "ordered": False,
                    },
                    {"name": "values", "type": "integer"},
                ],
                "primaryKey": ["index"],
            },
        ),
        (
            "data",
            [
                OrderedDict([("index", "a"), ("values", 1)]),
                OrderedDict([("index", "b"), ("values", 1)]),
            ],
        ),
    ]
)

assert result == expected
