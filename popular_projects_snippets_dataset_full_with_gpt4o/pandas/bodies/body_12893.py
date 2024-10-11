# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_json_table_schema.py
field = {"name": "foo"}
field.update(inp)
assert convert_json_field_to_pandas_type(field) == exp
