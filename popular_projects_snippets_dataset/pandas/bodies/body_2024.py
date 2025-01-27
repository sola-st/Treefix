# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_numeric.py
# GH#50505
if "pyarrow" in dtype:
    pytest.importorskip("pyarrow")
ser = Series([1, pd.NA], dtype=dtype)
result = to_numeric(ser, use_nullable_dtypes=True)
expected = Series([1, pd.NA], dtype=dtype)
tm.assert_series_equal(result, expected)
