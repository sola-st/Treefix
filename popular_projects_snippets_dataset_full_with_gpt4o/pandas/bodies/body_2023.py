# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_numeric.py
# GH#50505
if dtype_backend == "pyarrow":
    pytest.importorskip("pyarrow")
ser = Series([1, pd.NA], dtype="UInt64")
with option_context("mode.dtype_backend", dtype_backend):
    result = to_numeric(ser, use_nullable_dtypes=True, downcast="unsigned")
expected = Series([1, pd.NA], dtype=smaller)
tm.assert_series_equal(result, expected)
