# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
# GH 19342
# construction with a numpy scalar
# should not raise
result = Series(np.array(100), index=np.arange(4), dtype="int64")
expected = Series(100, index=np.arange(4), dtype="int64")
tm.assert_series_equal(result, expected)
