# Extracted from ./data/repos/pandas/pandas/tests/interchange/test_impl.py
df = pd.DataFrame(data)

df2 = df.__dataframe__()

assert df2.num_columns() == NCOLS
assert df2.num_rows() == NROWS

assert list(df2.column_names()) == list(data.keys())

indices = (0, 2)
names = tuple(list(data.keys())[idx] for idx in indices)

result = from_dataframe(df2.select_columns(indices))
expected = from_dataframe(df2.select_columns_by_name(names))
tm.assert_frame_equal(result, expected)

assert isinstance(result.attrs["_INTERCHANGE_PROTOCOL_BUFFERS"], list)
assert isinstance(expected.attrs["_INTERCHANGE_PROTOCOL_BUFFERS"], list)
