# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_json_table_schema.py
df = df_table
df.index.name = "idx"
result = df.to_json(orient="table", date_format="iso")
result = json.loads(result, object_pairs_hook=OrderedDict)

assert "pandas_version" in result["schema"]
result["schema"].pop("pandas_version")

fields = [
    {"name": "idx", "type": "integer"},
    {"name": "A", "type": "integer"},
    {"name": "B", "type": "string"},
    {"name": "C", "type": "datetime"},
    {"name": "D", "type": "duration"},
    {
        "constraints": {"enum": ["a", "b", "c"]},
        "name": "E",
        "ordered": False,
        "type": "any",
    },
    {
        "constraints": {"enum": ["a", "b", "c"]},
        "name": "F",
        "ordered": True,
        "type": "any",
    },
    {"name": "G", "type": "number"},
    {"name": "H", "type": "datetime", "tz": "US/Central"},
]

schema = {"fields": fields, "primaryKey": ["idx"]}
data = [
    OrderedDict(
        [
            ("idx", 0),
            ("A", 1),
            ("B", "a"),
            ("C", "2016-01-01T00:00:00.000"),
            ("D", "P0DT1H0M0S"),
            ("E", "a"),
            ("F", "a"),
            ("G", 1.0),
            ("H", "2016-01-01T06:00:00.000Z"),
        ]
    ),
    OrderedDict(
        [
            ("idx", 1),
            ("A", 2),
            ("B", "b"),
            ("C", "2016-01-02T00:00:00.000"),
            ("D", "P0DT1H1M0S"),
            ("E", "b"),
            ("F", "b"),
            ("G", 2.0),
            ("H", "2016-01-02T06:00:00.000Z"),
        ]
    ),
    OrderedDict(
        [
            ("idx", 2),
            ("A", 3),
            ("B", "c"),
            ("C", "2016-01-03T00:00:00.000"),
            ("D", "P0DT1H2M0S"),
            ("E", "c"),
            ("F", "c"),
            ("G", 3.0),
            ("H", "2016-01-03T06:00:00.000Z"),
        ]
    ),
    OrderedDict(
        [
            ("idx", 3),
            ("A", 4),
            ("B", "c"),
            ("C", "2016-01-04T00:00:00.000"),
            ("D", "P0DT1H3M0S"),
            ("E", "c"),
            ("F", "c"),
            ("G", 4.0),
            ("H", "2016-01-04T06:00:00.000Z"),
        ]
    ),
]
expected = OrderedDict([("schema", schema), ("data", data)])

assert result == expected
