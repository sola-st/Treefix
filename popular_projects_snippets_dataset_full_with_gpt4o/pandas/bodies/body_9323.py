# Extracted from ./data/repos/pandas/pandas/tests/arrays/masked/test_arrow_compat.py
df = pd.DataFrame({"a": data})
table = pa.table(df)
assert table.field("a").type == str(data.dtype.numpy_dtype)
result = table.to_pandas()
assert result["a"].dtype == data.dtype
tm.assert_frame_equal(result, df)
