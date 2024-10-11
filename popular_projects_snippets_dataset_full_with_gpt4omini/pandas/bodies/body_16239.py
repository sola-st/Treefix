# Extracted from ./data/repos/pandas/pandas/tests/series/test_logical_ops.py
# GH#22092, GH#19792 pre-2.0 these were aliased to setops
ser = Series([True, True, False, False])
idx1 = Index(
    [True, False, True, False], dtype=object
)  # TODO: raises if bool-dtype
idx2 = Index([1, 0, 1, 0])

expected = Series([False, True, True, False])
result = idx1 ^ ser
tm.assert_series_equal(result, expected)

result = idx2 ^ ser
tm.assert_series_equal(result, expected)
