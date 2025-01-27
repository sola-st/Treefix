# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_json_table_schema.py
kind = index_or_series
data = [1.0, 2.0, 3.0]
result = convert_pandas_type_to_json_field(kind(data, name="name"))
expected = {"name": "name", "type": "number"}
assert result == expected
