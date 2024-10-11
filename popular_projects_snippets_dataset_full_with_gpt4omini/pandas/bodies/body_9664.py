# Extracted from ./data/repos/pandas/pandas/tests/arrays/period/test_arrow_compat.py
from pandas.core.arrays.arrow.extension_types import ArrowPeriodType

arr = PeriodArray([1, 2, 3], freq="D")
arr[1] = pd.NaT
df = pd.DataFrame({"a": arr})

table = pa.table(df)
assert isinstance(table.field("a").type, ArrowPeriodType)
result = table.to_pandas()
assert isinstance(result["a"].dtype, PeriodDtype)
tm.assert_frame_equal(result, df)

table2 = pa.concat_tables([table, table])
result = table2.to_pandas()
expected = pd.concat([df, df], ignore_index=True)
tm.assert_frame_equal(result, expected)
