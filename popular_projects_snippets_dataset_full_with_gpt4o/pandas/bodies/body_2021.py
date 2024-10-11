# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_numeric.py
# GH#50505
if "pyarrow" in dtype:
    pytest.importorskip("pyarrow")
    dtype_backend = "pyarrow"
else:
    dtype_backend = "pandas"
ser = Series([val, None], dtype=object)
with option_context("mode.dtype_backend", dtype_backend):
    result = to_numeric(ser, use_nullable_dtypes=True)
expected = Series([val, pd.NA], dtype=dtype)
tm.assert_series_equal(result, expected)
