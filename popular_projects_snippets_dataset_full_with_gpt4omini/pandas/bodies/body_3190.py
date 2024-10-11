# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_asof.py
N = 50
rng = period_range("1/1/1990", periods=N, freq="H")
df = DataFrame(np.random.randn(N), index=rng)

# Mismatched freq
msg = "Input has different freq"
with pytest.raises(IncompatibleFrequency, match=msg):
    df.asof(rng.asfreq("D"))
