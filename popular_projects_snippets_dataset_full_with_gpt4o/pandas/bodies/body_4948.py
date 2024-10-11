# Extracted from ./data/repos/pandas/pandas/tests/reductions/test_reductions.py
# test idxmin
# _check_stat_op approach can not be used here because of isna check.
string_series = tm.makeStringSeries().rename("series")

# add some NaNs
string_series[5:15] = np.NaN

# skipna or no
assert string_series[string_series.idxmin()] == string_series.min()
assert isna(string_series.idxmin(skipna=False))

# no NaNs
nona = string_series.dropna()
assert nona[nona.idxmin()] == nona.min()
assert nona.index.values.tolist().index(nona.idxmin()) == nona.values.argmin()

# all NaNs
allna = string_series * np.nan
assert isna(allna.idxmin())

# datetime64[ns]
s = Series(date_range("20130102", periods=6))
result = s.idxmin()
assert result == 0

s[0] = np.nan
result = s.idxmin()
assert result == 1
