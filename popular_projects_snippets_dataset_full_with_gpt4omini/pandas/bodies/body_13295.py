# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
dtypes = {
    "TextCol": "str",
    "DateCol": "str",
    "IntDateCol": "int64",
    "IntDateOnlyCol": "int64",
    "FloatCol": "float",
    "IntCol": "int64",
    "BoolCol": "int64",
    "IntColWithNull": "float",
    "BoolColWithNull": "float",
}
df = DataFrame(types_data)
exit(df[dtypes.keys()].astype(dtypes))
