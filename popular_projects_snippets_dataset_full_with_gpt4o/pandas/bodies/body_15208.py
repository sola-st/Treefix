# Extracted from ./data/repos/pandas/pandas/tests/series/test_cumulative.py
# GH#28385
ser = pd.Series(
    [pd.Period("2012-1-1", freq="D"), pd.NaT, pd.Period("2012-1-2", freq="D")]
)
result = getattr(ser, func)(skipna=False)
expected = pd.Series([pd.Period("2012-1-1", freq="D"), pd.NaT, pd.NaT])
tm.assert_series_equal(result, expected)

result = getattr(ser, func)(skipna=True)
expected = pd.Series([pd.Period("2012-1-1", freq="D"), pd.NaT, exp])
tm.assert_series_equal(result, expected)
