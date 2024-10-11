# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_json_table_schema.py
# GH 19130
df = DataFrame(index=idx)
df.index.name = "index"
with tm.assert_produces_warning():
    set_default_names(df)
