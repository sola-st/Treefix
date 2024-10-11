# Extracted from ./data/repos/pandas/pandas/tests/arrays/string_/test_string.py
# GH-41040
import pyarrow as pa

data = pd.array([], dtype=dtype)
df = pd.DataFrame({"a": data})
table = pa.table(df)
assert table.field("a").type == "string"
# Instantiate the same table with no chunks at all
table = pa.table([pa.chunked_array([], type=pa.string())], schema=table.schema)
with pd.option_context("string_storage", string_storage2):
    result = table.to_pandas()
assert isinstance(result["a"].dtype, pd.StringDtype)
expected = df.astype(f"string[{string_storage2}]")
tm.assert_frame_equal(result, expected)
