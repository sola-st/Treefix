# Extracted from ./data/repos/pandas/pandas/tests/interchange/test_impl.py
test_str_data = string_data["separator data"] + [""]
df = pd.DataFrame({"A": test_str_data})
col = df.__dataframe__().get_column_by_name("A")

assert col.size() == 6
assert col.null_count == 1
assert col.dtype[0] == DtypeKind.STRING
assert col.describe_null == (ColumnNullType.USE_BYTEMASK, 0)

df_sliced = df[1:]
col = df_sliced.__dataframe__().get_column_by_name("A")
assert col.size() == 5
assert col.null_count == 1
assert col.dtype[0] == DtypeKind.STRING
assert col.describe_null == (ColumnNullType.USE_BYTEMASK, 0)
