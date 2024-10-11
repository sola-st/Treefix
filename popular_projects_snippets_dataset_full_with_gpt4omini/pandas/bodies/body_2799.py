# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_reindex.py
rng = date_range("1/1/2000 00:00:00", periods=10, freq="10s")
df = DataFrame({"A": np.random.randn(len(rng)), "B": rng})

result = df.reindex(range(15))
assert np.issubdtype(result["B"].dtype, np.dtype("M8[ns]"))

mask = com.isna(result)["B"]
assert mask[-5:].all()
assert not mask[:-5].any()
