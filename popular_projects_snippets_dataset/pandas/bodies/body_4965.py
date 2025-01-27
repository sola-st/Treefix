# Extracted from ./data/repos/pandas/pandas/tests/reductions/test_reductions.py
rng = date_range("1/1/2000", periods=10, freq="4h")
lvls = ["A", "A", "A", "B", "B", "B", "C", "C", "C", "C"]
df = DataFrame({"TS": rng, "V": np.random.randn(len(rng)), "L": lvls})

result = df.TS.max()
exp = Timestamp(df.TS.iat[-1])
assert isinstance(result, Timestamp)
assert result == exp

result = df.TS.min()
exp = Timestamp(df.TS.iat[0])
assert isinstance(result, Timestamp)
assert result == exp
