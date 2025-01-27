# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_json_table_schema.py
df = DataFrame(
    [[1, 2]], columns=[pd.Timestamp("2016"), pd.Timedelta(10, unit="s")]
)
result = df.to_json(orient="table")
js = json.loads(result)
assert js["schema"]["fields"][1]["name"] == "2016-01-01T00:00:00.000"
assert js["schema"]["fields"][2]["name"] == "P0DT0H0M10S"
