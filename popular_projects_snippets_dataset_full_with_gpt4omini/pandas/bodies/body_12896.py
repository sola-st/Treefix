# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_json_table_schema.py
data = pd.Series(1, idx)
result = set_default_names(data)
assert getattr(result.index, prop) == nm
