# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_convert_dtypes.py
# GH#48791
ser = pd.Series([1.5, pd.NA])
result = ser.convert_dtypes(infer_objects=infer_objects)
expected = pd.Series([1.5, pd.NA], dtype=dtype)
tm.assert_series_equal(result, expected)
