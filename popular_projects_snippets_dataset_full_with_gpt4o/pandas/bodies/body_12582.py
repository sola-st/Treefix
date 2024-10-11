# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_pandas.py
assert string_series.to_json() == string_series.to_json(orient="index")
