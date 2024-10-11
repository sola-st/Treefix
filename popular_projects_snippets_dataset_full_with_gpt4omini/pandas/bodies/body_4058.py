# Extracted from ./data/repos/pandas/pandas/tests/frame/test_reductions.py
# GH#676
assert df.values.dtype == np.object_
result = getattr(df, method)(1)
expected = getattr(df.astype("f8"), method)(1)
tm.assert_series_equal(result, expected)
