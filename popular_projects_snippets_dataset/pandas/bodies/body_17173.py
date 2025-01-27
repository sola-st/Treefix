# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_pivot.py
rng = date_range("1/1/2000", "12/31/2004", freq="M")
ts = Series(np.random.randn(len(rng)), index=rng)

annual = pivot_table(DataFrame(ts), index=ts.index.year, columns=ts.index.month)
annual.columns = annual.columns.droplevel(0)

month = ts.index.month
subset = ts[month == i]
subset.index = subset.index.year
result = annual[i].dropna()
tm.assert_series_equal(result, subset, check_names=False)
assert result.name == i
