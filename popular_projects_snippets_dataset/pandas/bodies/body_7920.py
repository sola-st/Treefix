# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/test_indexing.py
rng = period_range("2007-01", periods=50, freq="M")
ts = Series(np.random.randn(len(rng)), rng)

with pytest.raises(KeyError, match=r"^'2006'$"):
    ts["2006"]

result = ts["2008"]
assert (result.index.year == 2008).all()

result = ts["2008":"2009"]
assert len(result) == 24

result = ts["2008-1":"2009-12"]
assert len(result) == 24

result = ts["2008Q1":"2009Q4"]
assert len(result) == 24

result = ts[:"2009"]
assert len(result) == 36

result = ts["2009":]
assert len(result) == 50 - 24

exp = result
result = ts[24:]
tm.assert_series_equal(exp, result)

ts = pd.concat([ts[10:], ts[10:]])
msg = "left slice bound for non-unique label: '2008'"
with pytest.raises(KeyError, match=msg):
    ts[slice("2008", "2009")]
