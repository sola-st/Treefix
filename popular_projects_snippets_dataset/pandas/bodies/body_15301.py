# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_datetime.py

# diff freq
rng = date_range(datetime(2005, 1, 1), periods=20, freq="M")
ts = Series(np.arange(len(rng)), index=rng)
ts = ts.take(np.random.permutation(20))

result = ts["2005"]
for t in result.index:
    assert t.year == 2005
