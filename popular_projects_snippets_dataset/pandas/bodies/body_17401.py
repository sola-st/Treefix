# Extracted from ./data/repos/pandas/pandas/tests/interchange/test_impl.py
df = pd.DataFrame({"A": (test_data_categorical[data[0]])})

col = df.__dataframe__().get_column_by_name("A")
assert col.dtype[0] == DtypeKind.CATEGORICAL
assert col.null_count == 0
assert col.describe_null == (ColumnNullType.USE_SENTINEL, -1)
assert col.num_chunks() == 1
desc_cat = col.describe_categorical
assert desc_cat["is_ordered"] == data[1]
assert desc_cat["is_dictionary"] is True
assert isinstance(desc_cat["categories"], PandasColumn)
tm.assert_series_equal(
    desc_cat["categories"]._col, pd.Series(["a", "d", "e", "s", "t"])
)

tm.assert_frame_equal(df, from_dataframe(df.__dataframe__()))
