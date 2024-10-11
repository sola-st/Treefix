# Extracted from ./data/repos/pandas/pandas/tests/arrays/masked/test_arrow_compat.py
# GH-41040

df = pd.DataFrame({"a": data[0:0]})
table = pa.table(df)
assert table.field("a").type == str(data.dtype.numpy_dtype)
table = pa.table(
    [pa.chunked_array([], type=table.field("a").type)], schema=table.schema
)
result = table.to_pandas()
assert result["a"].dtype == data.dtype
tm.assert_frame_equal(result, df)
