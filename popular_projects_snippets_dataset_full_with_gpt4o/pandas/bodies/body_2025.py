# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_numeric.py
# GH#50505
if dtype_backend == "pyarrow":
    pytest.importorskip("pyarrow")
ser = Series(["a", "b", ""])
expected = ser.copy()
with pytest.raises(ValueError, match="Unable to parse string"):
    with option_context("mode.dtype_backend", dtype_backend):
        to_numeric(ser, use_nullable_dtypes=use_nullable_dtypes)

with option_context("mode.dtype_backend", dtype_backend):
    result = to_numeric(
        ser, use_nullable_dtypes=use_nullable_dtypes, errors="ignore"
    )
tm.assert_series_equal(result, expected)

with option_context("mode.dtype_backend", dtype_backend):
    result = to_numeric(
        ser, use_nullable_dtypes=use_nullable_dtypes, errors="coerce"
    )
if use_nullable_dtypes and dtype_backend == "pyarrow":
    dtype = "double[pyarrow]"
expected = Series([np.nan, np.nan, np.nan], dtype=dtype)
tm.assert_series_equal(result, expected)
