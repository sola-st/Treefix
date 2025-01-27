# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
rng = date_range("1/1/2000 00:00:00", "1/1/2000 1:59:50", freq="10s")
dates = np.asarray(rng)

series = Series(dates)
assert np.issubdtype(series.dtype, np.dtype("M8[ns]"))
