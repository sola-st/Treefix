# Extracted from ./data/repos/pandas/pandas/tests/arrays/interval/test_interval.py
import pyarrow as pa

from pandas.core.arrays.arrow.extension_types import ArrowIntervalType

arr = IntervalArray.from_breaks(breaks)
arr[1] = None
df = pd.DataFrame({"a": arr})

table = pa.table(df)
assert isinstance(table.field("a").type, ArrowIntervalType)
result = table.to_pandas()
assert isinstance(result["a"].dtype, pd.IntervalDtype)
tm.assert_frame_equal(result, df)

table2 = pa.concat_tables([table, table])
result = table2.to_pandas()
expected = pd.concat([df, df], ignore_index=True)
tm.assert_frame_equal(result, expected)

# GH-41040
table = pa.table(
    [pa.chunked_array([], type=table.column(0).type)], schema=table.schema
)
result = table.to_pandas()
tm.assert_frame_equal(result, expected[0:0])
