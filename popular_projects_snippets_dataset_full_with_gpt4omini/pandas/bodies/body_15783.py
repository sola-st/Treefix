# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_astype.py
result = Series([np.nan]).astype("period[D]")
expected = Series([NaT], dtype="period[D]")
tm.assert_series_equal(result, expected)
