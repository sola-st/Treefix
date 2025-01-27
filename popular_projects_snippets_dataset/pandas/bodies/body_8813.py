# Extracted from ./data/repos/pandas/pandas/tests/arrays/string_/test_string.py
# roundtrip possible from arrow 1.0.0
import pyarrow as pa

data = pd.array(["a", "b", None], dtype=dtype)
df = pd.DataFrame({"a": data})
table = pa.table(df)
assert table.field("a").type == "string"
with pd.option_context("string_storage", string_storage2):
    result = table.to_pandas()
assert isinstance(result["a"].dtype, pd.StringDtype)
expected = df.astype(f"string[{string_storage2}]")
tm.assert_frame_equal(result, expected)
# ensure the missing value is represented by NA and not np.nan or None
assert result.loc[2, "a"] is pd.NA
