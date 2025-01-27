# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_astype.py
# GH45798
result = Series([Timedelta(1), np.nan], dtype="timedelta64[ns]")
expected = Series([Timedelta(1), NaT], dtype="timedelta64[ns]")
tm.assert_series_equal(result, expected)
