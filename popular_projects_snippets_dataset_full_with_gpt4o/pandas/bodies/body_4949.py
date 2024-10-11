# Extracted from ./data/repos/pandas/pandas/tests/reductions/test_reductions.py
# test idxmax
# _check_stat_op approach can not be used here because of isna check.
string_series = tm.makeStringSeries().rename("series")

# add some NaNs
string_series[5:15] = np.NaN

# skipna or no
assert string_series[string_series.idxmax()] == string_series.max()
assert isna(string_series.idxmax(skipna=False))

# no NaNs
nona = string_series.dropna()
assert nona[nona.idxmax()] == nona.max()
assert nona.index.values.tolist().index(nona.idxmax()) == nona.values.argmax()

# all NaNs
allna = string_series * np.nan
assert isna(allna.idxmax())

s = Series(date_range("20130102", periods=6))
result = s.idxmax()
assert result == 5

s[5] = np.nan
result = s.idxmax()
assert result == 4

# Index with float64 dtype
# GH#5914
s = Series([1, 2, 3], [1.1, 2.1, 3.1])
result = s.idxmax()
assert result == 3.1
result = s.idxmin()
assert result == 1.1

s = Series(s.index, s.index)
result = s.idxmax()
assert result == 3.1
result = s.idxmin()
assert result == 1.1
