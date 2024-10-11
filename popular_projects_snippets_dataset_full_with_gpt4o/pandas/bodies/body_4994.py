# Extracted from ./data/repos/pandas/pandas/tests/reductions/test_stat_reductions.py
string_series = tm.makeStringSeries().rename("series")
datetime_series = tm.makeTimeSeries().rename("ts")

alt = lambda x: np.std(x, ddof=1) / np.sqrt(len(x))
self._check_stat_op("sem", alt, string_series)

result = datetime_series.sem(ddof=4)
expected = np.std(datetime_series.values, ddof=4) / np.sqrt(
    len(datetime_series.values)
)
tm.assert_almost_equal(result, expected)

# 1 - element series with ddof=1
s = datetime_series.iloc[[0]]
result = s.sem(ddof=1)
assert pd.isna(result)
