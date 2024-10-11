# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_rank.py
from scipy.stats import rankdata

datetime_series[::2] = np.nan
datetime_series[:10:3] = 4.0

ranks = datetime_series.rank()
oranks = datetime_series.astype("O").rank()

tm.assert_series_equal(ranks, oranks)

mask = np.isnan(datetime_series)
filled = datetime_series.fillna(np.inf)

# rankdata returns a ndarray
exp = Series(rankdata(filled), index=filled.index, name="ts")
exp[mask] = np.nan

tm.assert_series_equal(ranks, exp)

iseries = Series(np.arange(5).repeat(2))

iranks = iseries.rank()
exp = iseries.astype(float).rank()
tm.assert_series_equal(iranks, exp)
iseries = Series(np.arange(5)) + 1.0
exp = iseries / 5.0
iranks = iseries.rank(pct=True)

tm.assert_series_equal(iranks, exp)

iseries = Series(np.repeat(1, 100))
exp = Series(np.repeat(0.505, 100))
iranks = iseries.rank(pct=True)
tm.assert_series_equal(iranks, exp)

# Explicit cast to float to avoid implicit cast when setting nan
iseries = iseries.astype("float")
iseries[1] = np.nan
exp = Series(np.repeat(50.0 / 99.0, 100))
exp[1] = np.nan
iranks = iseries.rank(pct=True)
tm.assert_series_equal(iranks, exp)

iseries = Series(np.arange(5)) + 1.0
iseries[4] = np.nan
exp = iseries / 4.0
iranks = iseries.rank(pct=True)
tm.assert_series_equal(iranks, exp)

iseries = Series(np.repeat(np.nan, 100))
exp = iseries.copy()
iranks = iseries.rank(pct=True)
tm.assert_series_equal(iranks, exp)

# Explicit cast to float to avoid implicit cast when setting nan
iseries = Series(np.arange(5), dtype="float") + 1
iseries[4] = np.nan
exp = iseries / 4.0
iranks = iseries.rank(pct=True)
tm.assert_series_equal(iranks, exp)

rng = date_range("1/1/1990", periods=5)
# Explicit cast to float to avoid implicit cast when setting nan
iseries = Series(np.arange(5), rng, dtype="float") + 1
iseries.iloc[4] = np.nan
exp = iseries / 4.0
iranks = iseries.rank(pct=True)
tm.assert_series_equal(iranks, exp)

iseries = Series([1e-50, 1e-100, 1e-20, 1e-2, 1e-20 + 1e-30, 1e-1])
exp = Series([2, 1, 3, 5, 4, 6.0])
iranks = iseries.rank()
tm.assert_series_equal(iranks, exp)

# GH 5968
iseries = Series(["3 day", "1 day 10m", "-2 day", NaT], dtype="m8[ns]")
exp = Series([3, 2, 1, np.nan])
iranks = iseries.rank()
tm.assert_series_equal(iranks, exp)

values = np.array(
    [-50, -1, -1e-20, -1e-25, -1e-50, 0, 1e-40, 1e-20, 1e-10, 2, 40],
    dtype="float64",
)
random_order = np.random.permutation(len(values))
iseries = Series(values[random_order])
exp = Series(random_order + 1.0, dtype="float64")
iranks = iseries.rank()
tm.assert_series_equal(iranks, exp)
