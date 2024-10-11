# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_json_table_schema.py
int_data = [1, 2, 3]
assert as_json_table_type(np.array(int_data, dtype=int_type).dtype) == "integer"
