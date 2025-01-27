# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_pivot.py
rng = date_range("1/1/2000", "12/31/2004", freq="D")
ts = Series(np.random.randn(len(rng)), index=rng)

annual = pivot_table(
    DataFrame(ts), index=ts.index.year, columns=ts.index.dayofyear
)
annual.columns = annual.columns.droplevel(0)

doy = np.asarray(ts.index.dayofyear)

subset = ts[doy == i]
subset.index = subset.index.year

result = annual[i].dropna()
tm.assert_series_equal(result, subset, check_names=False)
assert result.name == i
