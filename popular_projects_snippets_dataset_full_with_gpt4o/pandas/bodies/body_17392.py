# Extracted from ./data/repos/pandas/pandas/tests/interchange/test_spec_conformance.py
df = df_from_dict({"a": [1, 2, 3]})
dfX = df.__dataframe__()
colX = dfX.get_column_by_name("a")
with pytest.raises(TypeError, match=".*categorical.*"):
    colX.describe_categorical
