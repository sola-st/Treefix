# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_pandas.py
# GH 17394
# Testing index=False in to_json with orient='table'

result = data.to_json(orient="table", index=False)
result = json.loads(result)

expected = {
    "schema": pd.io.json.build_table_schema(data, index=False),
    "data": DataFrame(data).to_dict(orient="records"),
}

assert result == expected
