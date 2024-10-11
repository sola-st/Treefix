# Extracted from ./data/repos/pandas/pandas/tests/arrays/period/test_arrow_compat.py
# GH-41040

from pandas.core.arrays.arrow.extension_types import ArrowPeriodType

arr = PeriodArray([], freq="D")
df = pd.DataFrame({"a": arr})

table = pa.table(df)
assert isinstance(table.field("a").type, ArrowPeriodType)
table = pa.table(
    [pa.chunked_array([], type=table.column(0).type)], schema=table.schema
)
result = table.to_pandas()
assert isinstance(result["a"].dtype, PeriodDtype)
tm.assert_frame_equal(result, df)
