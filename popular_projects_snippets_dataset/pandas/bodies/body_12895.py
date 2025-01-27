# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_json_table_schema.py
s = pd.Series(pd.Categorical(["a", "b", "a"]))
s.index.name = "idx"
result = s.to_json(orient="table", date_format="iso")
result = json.loads(result, object_pairs_hook=OrderedDict)
result["schema"].pop("pandas_version")

fields = [
    {"name": "idx", "type": "integer"},
    {
        "constraints": {"enum": ["a", "b"]},
        "name": "values",
        "ordered": False,
        "type": "any",
    },
]

expected = OrderedDict(
    [
        ("schema", {"fields": fields, "primaryKey": ["idx"]}),
        (
            "data",
            [
                OrderedDict([("idx", 0), ("values", "a")]),
                OrderedDict([("idx", 1), ("values", "b")]),
                OrderedDict([("idx", 2), ("values", "a")]),
            ],
        ),
    ]
)

assert result == expected
