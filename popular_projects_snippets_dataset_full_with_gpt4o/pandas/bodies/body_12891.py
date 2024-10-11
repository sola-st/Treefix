# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_json_table_schema.py
arr = pd.period_range("2016", freq="A-DEC", periods=4)
result = convert_pandas_type_to_json_field(arr)
expected = {"name": "values", "type": "datetime", "freq": "A-DEC"}
assert result == expected
