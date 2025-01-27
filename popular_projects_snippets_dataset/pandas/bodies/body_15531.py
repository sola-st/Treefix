# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_clip.py
"""Should process np.nan argument as None"""
# GH#17276
s = Series([1, 2, 3])

tm.assert_series_equal(s.clip(np.nan), Series([1, 2, 3]))
tm.assert_series_equal(s.clip(upper=np.nan, lower=np.nan), Series([1, 2, 3]))

# GH#19992
tm.assert_series_equal(s.clip(lower=[0, 4, np.nan]), Series([1, 4, 3]))
tm.assert_series_equal(s.clip(upper=[1, np.nan, 1]), Series([1, 2, 1]))

# GH#40420
s = Series([1, 2, 3])
result = s.clip(0, [np.nan, np.nan, np.nan])
tm.assert_series_equal(s, result)
