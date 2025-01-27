# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_setops.py
# GH43222
series1 = Series((1,), index=MultiIndex.from_tuples(((None, None),)))
series2 = Series((10, 20), index=MultiIndex.from_tuples(((None, None), ("a", "b"))))
result = DataFrame([series1, series2])
expected = DataFrame({(np.nan, np.nan): [1.0, 10.0], ("a", "b"): [np.nan, 20.0]})
tm.assert_frame_equal(result, expected)
