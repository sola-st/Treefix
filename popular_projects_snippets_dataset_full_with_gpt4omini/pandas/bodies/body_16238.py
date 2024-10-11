# Extracted from ./data/repos/pandas/pandas/tests/series/test_logical_ops.py
# GH#22092, GH#19792
ser = Series([True, True, False, False])
idx1 = Index([True, False, True, False])
idx2 = Index([1, 0, 1, 0])

expected = Series([op(ser[n], idx1[n]) for n in range(len(ser))])

result = op(ser, idx1)
tm.assert_series_equal(result, expected)

expected = Series([op(ser[n], idx2[n]) for n in range(len(ser))], dtype=bool)

result = op(ser, idx2)
tm.assert_series_equal(result, expected)
