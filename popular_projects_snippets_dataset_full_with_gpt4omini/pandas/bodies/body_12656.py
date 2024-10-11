# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_pandas.py
series = dataframe.stack()
result = series.to_json(orient="index")
assert result == expected
