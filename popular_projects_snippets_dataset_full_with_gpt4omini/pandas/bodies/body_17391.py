# Extracted from ./data/repos/pandas/pandas/tests/interchange/test_spec_conformance.py
df = df_from_dict({"a": [1.0, math.nan, 2.0]})
dfX = df.__dataframe__()
colX = dfX.get_column_by_name("a")
assert colX.null_count == 1
assert isinstance(colX.null_count, int)
