# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_json_table_schema.py
field = {"type": inp}
with pytest.raises(
    ValueError, match=f"Unsupported or invalid field type: {inp}"
):
    convert_json_field_to_pandas_type(field)
