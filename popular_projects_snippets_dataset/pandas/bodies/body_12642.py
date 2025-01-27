# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_pandas.py
# GH 17394
# Testing index=False in to_json with orient='split'

result = data.to_json(orient="split", index=False)
result = json.loads(result)

assert result == expected
