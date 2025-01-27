# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_datetime.py
# GH 2437
rng = date_range(start="2011-01-01", end="2011-01-15")
ts = Series(np.random.rand(len(rng)), index=rng)
ts2 = pd.concat([ts[0:4], ts[-4:], ts[4:-4]])

for t in ts.index:

    expected = ts[t]
    result = ts2[t]
    assert expected == result

# GH 3448 (ranges)
def compare(slobj):
    result = ts2[slobj].copy()
    result = result.sort_index()
    expected = ts[slobj]
    expected.index = expected.index._with_freq(None)
    tm.assert_series_equal(result, expected)

compare(slice("2011-01-01", "2011-01-15"))
with pytest.raises(KeyError, match="Value based partial slicing on non-monotonic"):
    compare(slice("2010-12-30", "2011-01-15"))
compare(slice("2011-01-01", "2011-01-16"))

# partial ranges
compare(slice("2011-01-01", "2011-01-6"))
compare(slice("2011-01-06", "2011-01-8"))
compare(slice("2011-01-06", "2011-01-12"))

# single values
result = ts2["2011"].sort_index()
expected = ts["2011"]
expected.index = expected.index._with_freq(None)
tm.assert_series_equal(result, expected)
