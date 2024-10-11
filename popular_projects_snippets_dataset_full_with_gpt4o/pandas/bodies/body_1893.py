# Extracted from ./data/repos/pandas/pandas/tests/resample/test_period_index.py
ts = simple_period_range_series("1/1/1990", "12/31/1995", freq="A-DEC")
df = DataFrame({"a": ts})
rdf = df.resample("D").ffill()
exp = df["a"].resample("D").ffill()
tm.assert_series_equal(rdf["a"], exp)

rng = period_range("2000", "2003", freq="A-DEC")
ts = Series([1, 2, 3, 4], index=rng)

result = ts.resample("M").ffill()
ex_index = period_range("2000-01", "2003-12", freq="M")

expected = ts.asfreq("M", how="start").reindex(ex_index, method="ffill")
tm.assert_series_equal(result, expected)
