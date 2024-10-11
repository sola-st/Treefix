# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_json_table_schema.py
bool_data = [True, False]
assert (
    as_json_table_type(np.array(bool_data, dtype=bool_type).dtype) == "boolean"
)
