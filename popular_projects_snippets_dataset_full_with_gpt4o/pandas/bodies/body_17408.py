# Extracted from ./data/repos/pandas/pandas/tests/interchange/test_impl.py
df = pd.DataFrame({"A": [pd.Timestamp("2022-01-01"), pd.NaT]})
col = df.__dataframe__().get_column_by_name("A")

assert col.size() == 2
assert col.null_count == 1
assert col.dtype[0] == DtypeKind.DATETIME
assert col.describe_null == (ColumnNullType.USE_SENTINEL, iNaT)

tm.assert_frame_equal(df, from_dataframe(df.__dataframe__()))
