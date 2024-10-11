# Extracted from ./data/repos/pandas/pandas/tests/series/test_subclass.py
N = 3
rng = pd.date_range("1/1/1990", periods=N, freq="53s")
s = tm.SubclassedSeries({"A": [np.nan, np.nan, np.nan]}, index=rng)

result = s.asof(rng[-2:])
assert isinstance(result, tm.SubclassedSeries)
