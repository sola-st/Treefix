# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_json_table_schema.py
data = [1.0, 2.0, 3.0]
data = pd.to_datetime(data, **dt_args)
if wrapper is pd.Series:
    data = pd.Series(data, name="values")
result = convert_pandas_type_to_json_field(data)
expected = {"name": "values", "type": "datetime"}
expected.update(extra_exp)
assert result == expected
