# Extracted from ./data/repos/pandas/pandas/tests/arrays/period/test_arrow_compat.py
arr = PeriodArray([1, 2, 3], freq="H")
arr[1] = pd.NaT
df = pd.DataFrame({"a": arr})

table = pa.table(df)
# remove the metadata
table = table.replace_schema_metadata()
assert table.schema.metadata is None

result = table.to_pandas()
assert isinstance(result["a"].dtype, PeriodDtype)
tm.assert_frame_equal(result, df)
