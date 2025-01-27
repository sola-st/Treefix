# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_json_table_schema.py
idx = pd.period_range("2016", freq="Q-JAN", periods=2)
data = pd.Series(1, idx)
result = data.to_json(orient="table", date_format="iso")
result = json.loads(result, object_pairs_hook=OrderedDict)
result["schema"].pop("pandas_version")

fields = [
    {"freq": "Q-JAN", "name": "index", "type": "datetime"},
    {"name": "values", "type": "integer"},
]

schema = {"fields": fields, "primaryKey": ["index"]}
data = [
    OrderedDict([("index", "2015-11-01T00:00:00.000"), ("values", 1)]),
    OrderedDict([("index", "2016-02-01T00:00:00.000"), ("values", 1)]),
]
expected = OrderedDict([("schema", schema), ("data", data)])

assert result == expected
