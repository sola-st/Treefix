# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_infer_objects.py
# GH#49650
ser = Series([b"a"], dtype="bytes")
expected = ser.copy()
result = ser.infer_objects()
tm.assert_series_equal(result, expected)
