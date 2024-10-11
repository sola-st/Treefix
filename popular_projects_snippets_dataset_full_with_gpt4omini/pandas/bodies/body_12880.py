# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_json_table_schema.py
assert as_json_table_type(pd.Categorical(["a"]).dtype) == "any"
assert as_json_table_type(CategoricalDtype()) == "any"
