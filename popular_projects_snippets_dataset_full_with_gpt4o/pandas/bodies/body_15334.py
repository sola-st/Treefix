# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_getitem.py
ser = Series(period_range("2000-01-01", periods=10, freq="D"))

result = ser[[2, 4]]
exp = Series(
    [pd.Period("2000-01-03", freq="D"), pd.Period("2000-01-05", freq="D")],
    index=[2, 4],
    dtype="Period[D]",
)
tm.assert_series_equal(result, exp)
assert result.dtype == "Period[D]"
