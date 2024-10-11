# Extracted from ./data/repos/pandas/pandas/tests/reductions/test_stat_reductions.py
string_series = tm.makeStringSeries().rename("series")
datetime_series = tm.makeTimeSeries().rename("ts")

alt = lambda x: np.std(x, ddof=1)
self._check_stat_op("std", alt, string_series)

alt = lambda x: np.var(x, ddof=1)
self._check_stat_op("var", alt, string_series)

result = datetime_series.std(ddof=4)
expected = np.std(datetime_series.values, ddof=4)
tm.assert_almost_equal(result, expected)

result = datetime_series.var(ddof=4)
expected = np.var(datetime_series.values, ddof=4)
tm.assert_almost_equal(result, expected)

# 1 - element series with ddof=1
s = datetime_series.iloc[[0]]
result = s.var(ddof=1)
assert pd.isna(result)

result = s.std(ddof=1)
assert pd.isna(result)
