# Extracted from ./data/repos/pandas/pandas/tests/series/test_logical_ops.py
# GH#22092, GH#19792
ser = Series([True, True, False, False])
idx1 = Index([True, False, True, False])
idx2 = Index([1, 0, 1, 0])

expected = Series(op(idx1.values, ser.values))
result = op(ser, idx1)
tm.assert_series_equal(result, expected)

expected = op(ser, Series(idx2))
result = op(ser, idx2)
tm.assert_series_equal(result, expected)
