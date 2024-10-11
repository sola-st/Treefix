# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
# GH10747
result = Series([np.nan]).astype("M8[ns]")
expected = Series([NaT])
tm.assert_series_equal(result, expected)
