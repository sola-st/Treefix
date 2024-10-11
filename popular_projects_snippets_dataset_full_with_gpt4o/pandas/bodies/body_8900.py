# Extracted from ./data/repos/pandas/pandas/tests/arrays/interval/test_interval.py
import pyarrow as pa

arr = IntervalArray.from_breaks(breaks)
arr[1] = None
df = pd.DataFrame({"a": arr})

table = pa.table(df)
# remove the metadata
table = table.replace_schema_metadata()
assert table.schema.metadata is None

result = table.to_pandas()
assert isinstance(result["a"].dtype, pd.IntervalDtype)
tm.assert_frame_equal(result, df)
