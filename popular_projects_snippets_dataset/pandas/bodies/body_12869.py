# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_json_table_schema.py
float_data = [1.0, 2.0, 3.0]
assert (
    as_json_table_type(np.array(float_data, dtype=float_type).dtype) == "number"
)
